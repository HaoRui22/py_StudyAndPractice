import ch10_oop

# 绑定属性时直接把属性暴露出去，便携简单但无法进行参数检查：
s = ch10_oop.student.Student()
s.score = 9999
print(f"分数{s.score}显然不合逻辑")