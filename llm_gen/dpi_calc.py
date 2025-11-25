
"""
dpi_mode_calc.py

计算在两种模式下（pixel / physical）从源分辨率+DPI 到 目标分辨率下的推荐 DPI。

Usage examples:
  # Pixel 模式（仅按像素对角比例缩放）
  python dpi_mode_calc.py --mode pixel --w1 1920 --h1 1080 --dpi1 1600 --w2 2560 --h2 1440

  # Physical 模式（按 PPI 比例，需要对角英寸）
  python dpi_mode_calc.py --mode physical --w1 1920 --h1 1080 --dpi1 1600 --w2 2560 --h2 1440 --d1 15.6 --d2 27

  # 如果 physical 模式但只知道源或目标的尺寸，可以用 --assume_same_physical 假设尺寸相同（效果等同于 pixel 模式）
  python dpi_mode_calc.py --mode physical --w1 1920 --h1 1080 --dpi1 1600 --w2 2560 --h2 1440 --d1 15.6 --assume_same_physical

Outputs:
  - 建议的新 DPI（浮点）
  - 最近的常见 DPI 档位建议（方便取整测试）
"""
import math
import argparse
from typing import Optional, List

COMMON_DPI = [200, 400, 800, 1200, 1600, 2000, 2400, 3200, 4800, 6400, 12000]

def diag_pixels(w: int, h: int) -> float:
    return math.hypot(w, h)

def ppi_from_res_and_diag(w: int, h: int, diag_inch: Optional[float]) -> Optional[float]:
    if diag_inch is None or diag_inch <= 0:
        return None
    return diag_pixels(w, h) / diag_inch

def nearest_common_dpis(value: float, n: int = 3) -> List[int]:
    # 返回最近的 n 个常见 DPI（按距离排序）
    diffs = sorted(((abs(value - d), d) for d in COMMON_DPI), key=lambda x: (x[0], x[1]))
    return [d for _, d in diffs[:n]]

def parse_args():
    p = argparse.ArgumentParser(description="在 pixel（像素）或 physical（物理/PPI）模式下计算目标 DPI")
    p.add_argument("--mode", choices=["pixel", "physical"], default="pixel",
                   help="计算模式：pixel（按像素对角比例）或 physical（按 PPI 比例）")
    p.add_argument("--w1", type=int, required=True, help="源分辨率宽 (px)")
    p.add_argument("--h1", type=int, required=True, help="源分辨率高 (px)")
    p.add_argument("--dpi1", type=float, required=True, help="源 DPI（当前鼠标 DPI）")
    p.add_argument("--w2", type=int, required=True, help="目标分辨率宽 (px)")
    p.add_argument("--h2", type=int, required=True, help="目标分辨率高 (px)")
    p.add_argument("--d1", type=float, default=None, help="源屏幕对角英寸 (inch)，physical 模式建议提供")
    p.add_argument("--d2", type=float, default=None, help="目标屏幕对角英寸 (inch)，physical 模式建议提供")
    p.add_argument("--assume_same_physical", action="store_true",
                   help="当缺少 d1/d2 时，假设两屏物理尺寸相同（使 physical 模式等同 pixel 模式）")
    return p.parse_args()

def calc_pixel_mode(w1,h1,dpi1,w2,h2) -> float:
    diag1 = diag_pixels(w1,h1)
    diag2 = diag_pixels(w2,h2)
    scale = diag2 / diag1
    return dpi1 * scale

def calc_physical_mode(w1,h1,dpi1,w2,h2,d1,d2, assume_same=False) -> Optional[float]:
    ppi1 = ppi_from_res_and_diag(w1,h1,d1)
    ppi2 = ppi_from_res_and_diag(w2,h2,d2)

    if ppi1 is None and ppi2 is None:
        if assume_same:
            # 退回到 pixel 模式
            return calc_pixel_mode(w1,h1,dpi1,w2,h2)
        else:
            return None
    if ppi1 is None or ppi2 is None:
        # 有一种 PPI 缺失 — 无法完成准确计算（除非假设相同物理）
        if assume_same:
            return calc_pixel_mode(w1,h1,dpi1,w2,h2)
        return None
    # DPI 比例等于 PPI 比例
    return dpi1 * (ppi2 / ppi1)

def main():
    args = parse_args()

    print("=== 输入 ===")
    print(f"模式: {args.mode}")
    print(f"源: {args.w1}x{args.h1}, DPI={args.dpi1}, 对角(inch)={args.d1}")
    print(f"目标: {args.w2}x{args.h2}, 对角(inch)={args.d2}")
    print("")

    if args.mode == "pixel":
        dpi2 = calc_pixel_mode(args.w1, args.h1, args.dpi1, args.w2, args.h2)
        print("模式说明: Pixel 模式（按分辨率像素对角比例缩放），与屏幕物理尺寸无关。")
        print(f"对角像素: 源={diag_pixels(args.w1,args.h1):.4f}, 目标={diag_pixels(args.w2,args.h2):.4f}")
        print(f"缩放系数 (diag_px_ratio) = {diag_pixels(args.w2,args.h2)/diag_pixels(args.w1,args.h1):.6f}")
    else:
        dpi2 = calc_physical_mode(args.w1, args.h1, args.dpi1, args.w2, args.h2, args.d1, args.d2, args.assume_same_physical)
        print("模式说明: Physical 模式（按像素密度 PPI 比例缩放，需屏幕对角英寸以计算 PPI）。")
        if dpi2 is None:
            print("错误: physical 模式需要源或目标的对角英寸 (d1/d2)。")
            print("你可以提供 --d1 和/或 --d2，或使用 --assume_same_physical 以假设两屏物理尺寸相同（退回到 pixel 模式）。")
            return
        ppi1 = ppi_from_res_and_diag(args.w1, args.h1, args.d1)
        ppi2 = ppi_from_res_and_diag(args.w2, args.h2, args.d2)
        print(f"PPI: 源={ppi1:.4f} px/in, 目标={ppi2:.4f} px/in")
        print(f"PPI 比例 (ppi2/ppi1) = {ppi2/ppi1:.6f}")

    print("")
    print("=== 结果 ===")
    print(f"建议 新 DPI (浮点) = {dpi2:.4f}")
    nearest = nearest_common_dpis(dpi2)
    print(f"附近常见 DPI 档位建议（最近 3 个）: {nearest}")
    print("")
    print("说明：实际使用时建议在鼠标驱动中选择最接近的可用档位并实际测试手感。若系统开启鼠标加速或显示缩放/游戏内灵敏度不同，主观感受会发生偏差。")

if __name__ == "__main__":
    main()
