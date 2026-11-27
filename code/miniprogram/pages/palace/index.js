const { PATHS } = require('../../services/api')

// 本页对应模块：palace（记忆宫殿），契约见 contracts/api.md
// 要接的端点（后端当前 501 骨架，W4 由 C 实现）：
// - GET  PATHS.palace.room          房间初始化/读取（F1）
// - POST PATHS.palace.itemCreate    摆放物品（F2）
// - POST PATHS.palace.itemLink      链接文件/笔记/错题（F3）
// - POST PATHS.palace.itemReview    点击复习（F4）
// 需要的状态：room.grid、items[]（grid_x/grid_y/z_index/link_type）、selectedItem
// TODO(A,W4)：先静态网格渲染 + 点击空态，接接口后补拖拽与失效灰态
Page({
  data: {
    title: '记忆宫殿',
    subtitle: '把资料摆进房间，变成可触摸的记忆锚点',
    emptyText: '房间还是空的，先摆第一件物品',
    actionText: '摆放物品',
    apiList: [PATHS.palace.room, PATHS.palace.itemCreate, PATHS.palace.itemReview]
  },

  onPrimaryTap() {
    wx.showToast({ title: 'W4 实现：摆放物品', icon: 'none' })
  }
})
