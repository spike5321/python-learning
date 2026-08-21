"""
Day 4：mockmate 实战 - 读简历 + 解析 JSON（含异常处理）
"""

import json
from pathlib import Path


def read_resume(file_path: str) -> str:
    """读简历文件（txt 格式），出错了不崩"""
    try:
        return Path(file_path).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"❌ 文件不存在：{file_path}")
        return ""
    except UnicodeDecodeError:
        print(f"❌ 文件编码错误，请用 UTF-8 保存")
        return ""
    except Exception as e:
        print(f"❌ 读文件出错了：{e}")
        return ""


def parse_skill_tags(resume_text: str) -> list[str]:
    """从简历里抽取技能标签（简化版）"""
    # 简单实现：找包含关键词的行
    keywords = ["Python", "Java", "LangChain", "RAG", "Agent", "React", "Docker"]
    found = []
    for kw in keywords:
        if kw.lower() in resume_text.lower():
            found.append(kw)
    return found


def build_candidate_profile(file_path: str) -> dict:
    """读简历 → 抽技能 → 打包成 dict（带异常处理）"""
    text = read_resume(file_path)
    if not text:
        return {"name": "未知", "skills": [], "error": "读文件失败"}

    return {
        "name": "候选人",
        "skills": parse_skill_tags(text),
        "resume_length": len(text),
    }


# === 测试 ===
print("测试 1: 读不存在的文件")
profile = build_candidate_profile("not_exist.txt")
print(f"结果：{profile}\n")

print("测试 2: 读自己")
profile = build_candidate_profile("day1.py")
print(f"找到的技能：{profile['skills']}\n")

print("测试 3: 模拟简历")
sample = """
张三
熟悉 Python、LangChain、RAG 开发
了解 Docker 和 React
"""
Path("sample_resume.txt").write_text(sample, encoding="utf-8")
profile = build_candidate_profile("sample_resume.txt")
print(f"结果：{profile}")