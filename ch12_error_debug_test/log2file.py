# 要让 logging 输出到日志文件,需要在 basicConfig 中添加 filename 和可能需要的 filemode 配置项。
# basicConfig 只能在程序中第一次调用时生效，因此务必放在代码最前面。
import logging

# 1. 创建 logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 2. 创建文件 Handler
file_handler = logging.FileHandler('log2file.log', mode='a' ,encoding='utf-8')
file_handler.setLevel(logging.INFO)

# 3. 创建控制台 Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 4. 统一日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 5. 绑定两个 Handler
logger.addHandler(file_handler)
logger.addHandler(console_handler)

s = '0'
n = int(s)
logger.info(f"n = {n}")   # 注意这里使用 logger 而不是 logging.info
print(10 / n)