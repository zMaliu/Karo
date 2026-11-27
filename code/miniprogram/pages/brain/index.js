const { PATHS } = require('../../services/api')

// 本页对应模块：brain（智脑），契约见 contracts/api.md
// 要接的端点（后端当前 501 骨架，W4 由 B 实现）：
// - POST PATHS.brain.fileUpload  上传并解析文件（F1）
// - POST PATHS.brain.noteCreate  写 Markdown 笔记（F2）
// - GET  PATHS.brain.noteDetail  笔记详情（F2）
// - POST PATHS.brain.chat        带引用的资料问答（F4）
// 需要的状态：notes[]、files[]、chatMessages[]、activeTab(file/note/diary)
// TODO(A,W4)：接笔记列表 + 问答（无命中时展示“本人资料中未找到”）
Page({
  data: {
    title: '学习大脑',
    subtitle: '个人资料仓库 · 带引用的本人资料问答',
    emptyText: '大脑还是空的，先写第一篇笔记',
    actionText: '写笔记',
    apiList: [PATHS.brain.fileUpload, PATHS.brain.noteCreate, PATHS.brain.chat]
  },

  onPrimaryTap() {
    wx.showToast({ title: 'W4 实现：写笔记', icon: 'none' })
  }
})
