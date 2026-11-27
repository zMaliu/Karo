"""brain 服务层声明：函数签名 + 实现步骤要点，业务待团队实现（规格书 §4）。

当前所有函数体只有 raise NotImplementedError（路由暂未调用），
由 app/common/errors.py 的 NotImplementedError handler 统一转 501。
"""


def upload_file(user_id, payload):
    """BRN-01：上传并解析文件。

    实现步骤：
    1. 校验格式白名单（pdf/image/word/txt）与 ≤20MB，按 hash 去重。
    2. 先落本地/对象存储，写 brain_file(parse_status=parsing)。
    3. 异步解析文本 → 切片写 brain_chunk → parse_status=ok；失败标记 failed 可重试。
    """
    raise NotImplementedError("brain.upload_file 待实现（BRN-01）")

def list_files(user_id, params):
    """BRN-05：文件列表 / 搜索筛选。

    实现步骤：
    1. 按 user_id + 可选 keyword/tag/type 过滤。
    2. 分页返回 items 与 total；空结果由前端给空态。
    """
    raise NotImplementedError("brain.list_files 待实现（BRN-05）")

def get_file(user_id, file_id):
    """BRN-01：文件详情与切片。

    实现步骤：
    1. 按 user_id + id 查 brain_file，越权统一 404。
    2. 附带 brain_chunk 切片摘要与来源信息。
    """
    raise NotImplementedError("brain.get_file 待实现（BRN-01）")

def create_note(user_id, payload):
    """BRN-02：写 Markdown 笔记。

    实现步骤：
    1. 校验标题非空、正文 ≤2 万字。
    2. 写 brain_note，并异步生成摘要切片写入 brain_chunk。
    """
    raise NotImplementedError("brain.create_note 待实现（BRN-02）")

def get_note(user_id, note_id):
    """BRN-02：笔记详情。

    实现步骤：
    1. 按 user_id + id 查 brain_note，越权 404。
    2. 返回正文、标签与关联切片。
    """
    raise NotImplementedError("brain.get_note 待实现（BRN-02）")

def update_note(user_id, note_id, payload):
    """BRN-06：编辑笔记 / 自动草稿。

    实现步骤：
    1. 按 user_id + id 查笔记，越权 404。
    2. 只更新传入字段；自动草稿与正式保存共用本接口。
    3. 并发编辑冲突保留版本提示。
    """
    raise NotImplementedError("brain.update_note 待实现（BRN-06）")

def create_diary(user_id, payload):
    """BRN-03：写学习日记。

    实现步骤：
    1. 校验日期与正文非空；一天可写多篇。
    2. 写 brain_diary；心情标签供 twin 对话上下文使用。
    """
    raise NotImplementedError("brain.create_diary 待实现（BRN-03）")

def list_diaries(user_id, params):
    """BRN-03：日记时间线。

    实现步骤：
    1. 按 user_id + 日期范围查 brain_diary 时间线。
    2. 分页返回 items；默认仅本人可见。
    """
    raise NotImplementedError("brain.list_diaries 待实现（BRN-03）")

def chat(user_id, payload):
    """BRN-04：带引用的资料问答。

    实现步骤：
    1. question 向量化 → 在本人 brain_chunk 做 Top-K 召回。
    2. 组装 RAG Prompt → LLM 流式作答 → 标注引用片段 → 审核返回。
    3. 召回为空明确回答「本人资料中未找到」，不臆造；引用与回答分离展示。
    """
    raise NotImplementedError("brain.chat 待实现（BRN-04）")
