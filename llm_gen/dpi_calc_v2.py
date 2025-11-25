
"""
dpi_interactive.py

交互式命令行工具：在 pixel / physical 两种模式下计算目标 DPI，
支持单次计算、批量计算与 CSV 导出，提供最近常见 DPI 建议。

运行:
    python dpi_interactive.py
"""

import math
import csv
import os
from typing import Optional, List, Tuple

COMMON_DPI = [200, 400, 800, 1200, 1600, 2000, 2400, 3200, 4800, 6400, 12000]

def diag_pixels(w: int, h: int) -> float:
    return math.hypot(w, h)

def ppi_from_res_and_diag(w: int, h: int, diag_inch: Optional[float]) -> Optional[float]:
    if diag_inch is None or diag_inch <= 0:
        return None
    return diag_pixels(w, h) / diag_inch

def nearest_common_dpis(value: float, n: int = 3) -> List[int]:
    diffs = sorted(((abs(value - d), d) for d in COMMON_DPI), key=lambda x: (x[0], x[1]))
    return [d for _, d in diffs[:n]]

def calc_pixel_mode(w1:int,h1:int,dpi1:float,w2:int,h2:int) -> float:
    diag1 = diag_pixels(w1,h1)
    diag2 = diag_pixels(w2,h2)
    scale = diag2 / diag1
    return dpi1 * scale

def calc_physical_mode(w1:int,h1:int,dpi1:float,w2:int,h2:int,d1:Optional[float],d2:Optional[float], assume_same=False) -> Optional[float]:
    ppi1 = ppi_from_res_and_diag(w1,h1,d1)
    ppi2 = ppi_from_res_and_diag(w2,h2,d2)
    if ppi1 is None and ppi2 is None:
        if assume_same:
            return calc_pixel_mode(w1,h1,dpi1,w2,h2)
        return None
    if ppi1 is None or ppi2 is None:
        if assume_same:
            return calc_pixel_mode(w1,h1,dpi1,w2,h2)
        return None
    return dpi1 * (ppi2 / ppi1)

def input_int(prompt:str, default:Optional[int]=None) -> int:
    while True:
        s = input(prompt).strip()
        if s == "" and default is not None:
            return default
        try:
            v = int(s)
            return v
        except Exception:
            print("输入必须是整数，请重试（或按 Enter 使用默认）。")

def input_float(prompt:str, default:Optional[float]=None, allow_empty:bool=False) -> Optional[float]:
    while True:
        s = input(prompt).strip()
        if s == "" and default is not None:
            return default
        if s == "" and allow_empty:
            return None
        try:
            v = float(s)
            return v
        except Exception:
            print("输入必须是数字，请重试（或按 Enter 使用默认/留空）。")

def ask_yesno(prompt:str, default:bool=True) -> bool:
    choices = "Y/n" if default else "y/N"
    while True:
        s = input(f"{prompt} ({choices}): ").strip().lower()
        if s == "" and default is not None:
            return default
        if s in ("y","yes"):
            return True
        if s in ("n","no"):
            return False
        print("请输入 y 或 n。")

def format_result(dpi2:float) -> str:
    nearest = nearest_common_dpis(dpi2)
    return f"建议新 DPI = {dpi2:.4f}，附近常见档位：{nearest}"

def single_calc_interactive(defaults:dict):
    print("\n--- 单次计算 ---")
    mode = ""
    while mode not in ("pixel","physical"):
        mode = input("选择模式 (pixel / physical) [pixel]: ").strip().lower() or "pixel"
    w1 = input_int(f"源分辨率宽 (px) [{defaults['w1']}]: ", default=defaults['w1'])
    h1 = input_int(f"源分辨率高 (px) [{defaults['h1']}]: ", default=defaults['h1'])
    dpi1 = input_float(f"源 DPI [{defaults['dpi1']}]: ", default=defaults['dpi1'])
    w2 = input_int(f"目标分辨率宽 (px) [{defaults['w2']}]: ", default=defaults['w2'])
    h2 = input_int(f"目标分辨率高 (px) [{defaults['h2']}]: ", default=defaults['h2'])
    d1 = input_float("源屏幕对角英寸 (inch)（可选，留空表示未知）: ", allow_empty=True)
    d2 = input_float("目标屏幕对角英寸 (inch)（可选，留空表示未知）: ", allow_empty=True)
    assume_same = False
    if mode == "physical":
        if d1 is None or d2 is None:
            assume_same = ask_yesno("缺少对角英寸。是否假设两屏物理尺寸相同（退回到 pixel 模式）？", default=True)

    if mode == "pixel":
        dpi2 = calc_pixel_mode(w1,h1,dpi1,w2,h2)
        print("\n[Pixel 模式] 说明：按像素对角比例缩放，忽略物理尺寸。")
        print(f"源对角像素 = {diag_pixels(w1,h1):.4f}, 目标对角像素 = {diag_pixels(w2,h2):.4f}")
    else:
        dpi2 = calc_physical_mode(w1,h1,dpi1,w2,h2,d1,d2, assume_same)
        if dpi2 is None:
            print("无法在 physical 模式下计算（缺少对角英寸且未选择假设相同物理）。")
            return
        ppi1 = ppi_from_res_and_diag(w1,h1,d1)
        ppi2 = ppi_from_res_and_diag(w2,h2,d2)
        print("\n[Physical 模式] 说明：按 PPI 比例缩放以保持物理移动感受。")
        print(f"PPI 源 = {ppi1:.4f} px/in, 目标 = {ppi2:.4f} px/in")

    print(format_result(dpi2))
    # 更新 defaults
    defaults.update({"w1":w1,"h1":h1,"w2":w2,"h2":h2,"dpi1":dpi1})
    return {"mode":mode,"w1":w1,"h1":h1,"dpi1":dpi1,"w2":w2,"h2":h2,"d1":d1,"d2":d2,"dpi2":dpi2}

def batch_calc_interactive(defaults:dict) -> List[dict]:
    print("\n--- 批量计算 ---")
    mode = ""
    while mode not in ("pixel","physical"):
        mode = input("选择模式 (pixel / physical) [pixel]: ").strip().lower() or "pixel"
    w1 = input_int(f"源分辨率宽 (px) [{defaults['w1']}]: ", default=defaults['w1'])
    h1 = input_int(f"源分辨率高 (px) [{defaults['h1']}]: ", default=defaults['h1'])
    dpi1 = input_float(f"源 DPI [{defaults['dpi1']}]: ", default=defaults['dpi1'])
    d1 = input_float("源屏幕对角英寸 (inch)（可选，留空表示未知）: ", allow_empty=True)
    assume_same = False
    if mode == "physical" and d1 is None:
        assume_same = ask_yesno("缺少源对角英寸。是否假设两屏物理尺寸相同（退回到 pixel 模式）？", default=True)

    entries = []
    print("请输入目标分辨率（一行一个，格式 width,height）。完成输入空行结束。示例：2560,1440")
    while True:
        line = input("目标分辨率: ").strip()
        if line == "":
            break
        try:
            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 2:
                raise ValueError
            w2 = int(parts[0]); h2 = int(parts[1])
        except Exception:
            print("格式错误，请输入 width,height（例如 2560,1440）或空行结束。")
            continue
        d2 = None
        if mode == "physical":
            d2 = input_float("目标屏幕对角英寸 (inch)（可选，留空表示未知）: ", allow_empty=True)
            if d2 is None and not assume_same:
                use_same = ask_yesno("目标对角未知。是否对该条目假设物理相同？（否则跳过此条目）", default=True)
                if not use_same:
                    print("跳过该条目。")
                    continue
        if mode == "pixel":
            dpi2 = calc_pixel_mode(w1,h1,dpi1,w2,h2)
        else:
            dpi2 = calc_physical_mode(w1,h1,dpi1,w2,h2,d1,d2, assume_same)
            if dpi2 is None:
                print("无法在 physical 模式下计算此条目（缺少必要对角英寸），已跳过。")
                continue
        entry = {"w2":w2,"h2":h2,"d2":d2,"dpi2":dpi2}
        entries.append(entry)
        print("结果：", format_result(dpi2))
    return entries

def export_csv(entries:List[dict], filename:str, header_extra:Optional[List[Tuple[str,str]]]=None):
    fieldnames = ["w2","h2","d2","dpi2"]
    try:
        with open(filename,"w",newline="",encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for e in entries:
                writer.writerow({
                    "w2": e.get("w2"),
                    "h2": e.get("h2"),
                    "d2": e.get("d2") if e.get("d2") is not None else "",
                    "dpi2": f"{e.get('dpi2'):.4f}"
                })
        print(f"已导出 CSV: {filename}")
    except Exception as ex:
        print("导出失败：", ex)

def print_welcome():
    print("="*60)
    print("鼠标 DPI 适配 交互式工具")
    print("模式说明：")
    print("  pixel    - 按分辨率像素对角比例缩放（忽略物理尺寸）")
    print("  physical - 按 PPI（pixels per inch）比例缩放（保持物理移动感受）")
    print("快捷命令：single (单次), batch (批量), exit (退出), help (显示提示)")
    print("="*60)

def main():
    defaults = {"w1":1920,"h1":1080,"w2":2560,"h2":1440,"dpi1":1600}
    history = []
    print_welcome()
    while True:
        cmd = input("\n输入命令 (single / batch / history / export / help / exit): ").strip().lower()
        if cmd in ("q","quit","exit"):
            print("退出。")
            break
        if cmd in ("h","help"):
            print_welcome()
            continue
        if cmd == "single":
            rec = single_calc_interactive(defaults)
            if rec:
                history.append(rec)
            continue
        if cmd == "batch":
            entries = batch_calc_interactive(defaults)
            if entries:
                # 将批量条目写入 history，每条作为记录
                for e in entries:
                    history.append({"mode":"batch","w2":e["w2"],"h2":e["h2"],"d2":e["d2"],"dpi2":e["dpi2"]})
            continue
        if cmd == "history":
            if not history:
                print("历史记录为空。")
                continue
            print("=== 历史 ===")
            for i,rec in enumerate(history,1):
                if rec.get("mode") == "batch":
                    print(f"{i}. target {rec.get('w2')}x{rec.get('h2')}, d2={rec.get('d2')}, dpi2={rec.get('dpi2'):.4f}")
                else:
                    print(f"{i}. mode={rec.get('mode')}, {rec.get('w1')}x{rec.get('h1')}@{rec.get('dpi1')} -> {rec.get('w2')}x{rec.get('h2')}, dpi2={rec.get('dpi2'):.4f}")
            continue
        if cmd == "export":
            if not history:
                print("没有历史记录可导出。请先执行 single 或 batch。")
                continue
            fname = input("输入导出文件名 (默认 dpi_results.csv): ").strip() or "dpi_results.csv"
            # 转换历史为表格行
            rows = []
            for rec in history:
                if rec.get("mode") == "batch":
                    rows.append({"w2":rec.get("w2"),"h2":rec.get("h2"),"d2":rec.get("d2"),"dpi2":rec.get("dpi2")})
                else:
                    rows.append({"w2":rec.get("w2"),"h2":rec.get("h2"),"d2":rec.get("d1") if rec.get("d1") is not None else "", "dpi2":rec.get("dpi2")})
            export_csv(rows, fname)
            continue
        print("未知命令。可用命令: single, batch, history, export, help, exit")

if __name__ == "__main__":
    main()
