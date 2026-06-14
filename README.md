# PNG To Frontend Rebuild

把一张或多张 PNG/JPG/WEBP UI 截图，重建成可运行、可截图校准、可继续开发的前端项目。

这个 skill 面向 Codex、Cursor、Trae、Claude Code 等支持本地技能目录的 AI 编程助手。它不是“截图切片工具”，而是一套高保真重建流程：先识别复杂视觉资产，再用 Image-2 或可用图像模型生成/编辑资产，最后用真实 HTML/CSS/JS 或项目框架实现界面，并通过浏览器截图和标尺对比反复校准。

---

## 它解决什么问题

很多“截图转前端”失败，不是因为代码写不出来，而是因为 AI 偷懒把复杂图标、会员等级、Hero 图、装饰物、底部导航图标、右上角操作图标都当成普通 CSS 或随手裁图处理。结果页面能打开，但和原图差距很大。

这个 skill 把这些容易出错的地方变成硬性流程：

- 复杂图标和装饰资产必须逐项盘点。
- 用户要求使用 Image-2 时，必须真的用 Image-2/图像模型生成对应资产。
- 不允许把原图图标裁出来冒充“重绘”。
- 手机截图默认不复刻系统通知栏、电量栏和 Home Indicator。
- 高保真交付前必须做浏览器截图和标尺对比。
- 文本、布局、按钮、列表、表单等普通 UI 必须用真实 DOM/CSS 实现，方便后续开发。

---

## 核心能力

- **资产规划**：先生成资产决策表，明确哪些用图像模型、哪些提取、哪些用 CSS/DOM。
- **Image-2 优先**：适合会员等级、服务图标、徽章、插画、Hero 图、底部导航图标等自定义视觉资产。
- **禁止伪还原**：不把截图切块当组件，不把截取图标当“重绘”。
- **移动端截图规则**：默认忽略手机系统状态栏，只还原产品 UI。
- **标尺校准**：提供 `make_ruler_compare.py`，支持横向/纵向辅助线，用于逐像素观察差异。
- **框架适配**：支持静态 HTML、React、Vue、Next.js、Tailwind、shadcn/ui、小程序/UniApp 等项目场景。
- **可继续开发**：最终产物是可维护的前端代码和独立资产，而不是一张大背景图。

---

## 仓库结构

```text
png-to-frontend-rebuild/
├─ README.md
├─ VERSION
├─ CHANGELOG.md
└─ png-to-frontend-rebuild/
   ├─ SKILL.md
   ├─ agents/
   │  └─ openai.yaml
   ├─ assets/
   │  └─ html-template/
   ├─ references/
   │  ├─ asset-planning.md
   │  ├─ calibration.md
   │  ├─ framework-adapters.md
   │  ├─ project-case-miniapp.md
   │  └─ workflow.md
   └─ scripts/
      └─ make_ruler_compare.py
```

---

## 安装

### Codex

把 `png-to-frontend-rebuild/` 这个 skill 文件夹复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse .\png-to-frontend-rebuild "$env:USERPROFILE\.codex\skills\png-to-frontend-rebuild"
```

重启 Codex，或开启新的 Codex 会话后即可使用。

### 其他 AI IDE

把仓库中的 `png-to-frontend-rebuild/` skill 文件夹复制到对应工具的 skills 目录，例如：

```text
~/.codex/skills/png-to-frontend-rebuild
~/.cursor/skills/png-to-frontend-rebuild
~/.trae/skills/png-to-frontend-rebuild
~/.claude/skills/png-to-frontend-rebuild
```

如果对应目录不存在，先手动创建。

---

## 快速开始

在 AI 助手里直接点名这个 skill，并提供设计截图：

```text
使用 $png-to-frontend-rebuild，把 C:\Users\me\Downloads\home.png 重建成一个可运行的移动端 HTML 页面。
需要高保真，复杂图标、会员等级、Hero 图都用 Image-2 生成，不要裁原图图标。
```

更完整的请求示例：

```text
使用 $png-to-frontend-rebuild 重建这组小程序截图：
- 首页：C:\design\home.png
- 会员页：C:\design\vip.png
- 我的页：C:\design\profile.png

要求：
1. 用 React + Tailwind。
2. 底部导航、会员等级、服务图标、右上角图标都作为独立资产处理。
3. 手机系统状态栏不要还原。
4. 完成后给我本地预览地址、浏览器截图和标尺对比图。
```

---

## 推荐的 Image-2 配置方式

如果你的运行环境支持 OpenAI Responses / Image-2，可以在你的工具配置中指定图像模型。不要把真实 API key 提交到仓库；请使用本机环境变量、密钥管理器或工具自带的安全配置。

这个 skill 的原则是：

- 用户明确要求 Image-2 时，自定义图标和复杂装饰资产必须使用 Image-2 或声明阻塞原因。
- 生成图标时优先产出透明背景 PNG/WebP。
- 如果用 sprite sheet，必须拆分、去背景、裁透明边界，再放入真实 UI 校验。
- 不允许把带方框、底色、标签、网格线的生成图直接塞进界面。

---

## 工作流

1. 检查输入截图和目标项目。
2. 读取 `references/workflow.md` 和 `references/asset-planning.md`。
3. 输出执行计划和资产决策表。
4. 生成、提取或整理必要视觉资产。
5. 用目标技术栈实现真实前端。
6. 启动本地预览并截图。
7. 使用标尺对比图或测量表校准。
8. 迭代布局、字体、图标、图片和响应式细节。
9. 在最终回复中列出文件、预览地址、截图、对比图和剩余差距。

---

## 资产决策表

每次高保真重建前，AI 都应该先给出类似表格：

| assetId | sourcePage | visualRole | strategy | reason | promptNeeded | outputPath | status | risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hero-phone | home | Hero 手机图 | image-model-required | 复杂产品图，不适合 CSS | yes | assets/hero-phone.png | planned | high |
| vip-level-gold | vip | 会员等级图标 | image-model-required | 自定义质感图标 | yes | assets/vip-level-gold.png | planned | medium |
| qr-code | invite | 二维码 | extract-user-asset | 必须保持精确可扫 | no | assets/qr-code.png | needed | high |
| tab-button | all | 底部导航文字与布局 | css-dom | 文本和状态可编辑 | no | component | planned | low |

策略说明：

- `image-model-required`：用 Image-2 或可用图像模型生成。
- `extract-user-asset`：提取必须精确保留的用户资产，例如二维码、真实头像、官方 logo。
- `css-dom`：用代码实现普通 UI，例如文字、卡片、按钮、网格、表单。
- `hybrid`：图像皮肤加 live DOM 文本或交互。

---

## 标尺对比

skill 内置脚本可生成源图与实现截图的横向对比，并叠加辅助线：

```powershell
python .\png-to-frontend-rebuild\scripts\make_ruler_compare.py `
  --source .\source.png `
  --actual .\screenshot.png `
  --out .\compare.png `
  --mark 120 --mark 360 `
  --vmark 80 --vmark 240
```

高保真任务完成前，至少应该产出一次对比图，并根据对比结果做一轮修正。

---

## 预期交付物

一次完整重建通常应该包含：

- 可运行的前端页面或项目代码。
- 生成/提取后的独立资产文件。
- 本地预览地址或可打开的 HTML 文件路径。
- 浏览器截图。
- 标尺对比图或测量说明。
- 未完成差距清单，按布局、资产、文字、交互、响应式、源图歧义、模型/工具阻塞分类。

---

## 版本管理

建议带版本号发布。这个仓库从 `v0.1.0` 开始：

- `0.x`：流程仍在快速迭代，可能继续补强规则和脚本。
- `0.1.x`：修复文档、规则、脚本的小问题。
- `0.x.0`：新增明显能力，例如新的校准脚本、框架适配策略、资产生成流程。
- `1.0.0`：当流程在多类真实项目中稳定通过后，再标记为稳定版。

---

## 适合谁使用

- 想把 App、小程序、网页截图重建成真实前端的人。
- 需要 AI 严格执行高保真流程，而不是随手生成近似页面的人。
- 需要把设计稿中的复杂图标、会员等级、服务入口、Hero 图逐项重绘/生成的人。
- 想把失败经验沉淀成可复用 Codex skill 的团队。

---

## 注意

这个 skill 不是版权绕过工具。对于官方 logo、人物肖像、二维码、真实商品图、地图、图表等需要精确保留或涉及权利风险的资产，应使用用户提供的原始素材或明确授权的资源。
