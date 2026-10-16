> 本评测现已收录到通用评测仓库：[pexoai/ai-evaluations](https://github.com/pexoai/ai-evaluations/tree/main/evaluations/wildlife-photography-2026)。后续新增评测统一放在那里，本仓库保留原实验记录。

# AI和人类评委为什么选得不一样？

一次野生动物摄影评选实验：用第62届成年组公开获奖材料重建16件候选，让四个多模态模型独立选择年度冠军，再与人类评委的选择对照。

**这里公开评测方式、提示词、作品来源清单、图片校验值和完整评语。原图版权属于摄影师，不随仓库分发。** 本仓库是探索性实验，非官方赛事项目，也不是模型审美排行榜。

## 自己评一次

1. 按 [作品清单](dataset/manifest.json) 中的官方页面取得16张可合法使用的图片，命名为C01.jpg—C16.jpg，放到本机`images/`。
2. 运行 `python3 scripts/verify.py --images images` 核对是否与本次输入一致。哈希不同不等于图错，但不能声称字节级复现。
3. 新建独立聊天，关闭联网，上传16张图片和 [英文说明](dataset/captions-input.en.txt)，粘贴 [评选提示词](prompts/judge.zh.txt)。确认模型实际读取全部图片。
4. 保存完整回答和运行设置，先选出自己的冠军，再查看下面的实验结果。

也可运行 `python3 scripts/prepare.py --images images --out model-input`，在本机生成只含图片、英文说明和提示词的输入包；不会包含维护方映射或答案。压缩包必须确认聊天工具可解压并实际查看图像，否则逐图上传。

## 仓库内容

- [评测方法与限制](docs/methodology.md)：候选范围、评价维度、运行设置与可解释范围。
- [作品清单](dataset/manifest.json)：16件作品、作者、官方链接、SHA-256与组照代理标记。
- [共同提示词](prompts/judge.zh.txt) 与 [本轮实际英文输入](dataset/captions-input.en.txt)。
- [完整模型报告](results/reports/) 与 [结构化结果](results/run-2026-10-14.json)。
- [来源与权利说明](docs/rights-and-sources.md)。

<details><summary>展开本轮结果（建议先自己评）</summary>

GPT与Gemini选了《Making Morays》（海鳝），Opus与Seed选了《Warning Sign》（美洲狮）。人类评委选出的年度冠军是《The Aftermath》（大象）。GPT与Gemini也将官方冠军排进前三。[查看结果对照](results/summary.md)。

</details>

## 需要知道的限制

16张中有3张是获奖组照公开展示代表图，未证实为评委内部指定单幅。因此不是已确认的官方最终候选池。每模型仅一次成功评选，输入保留署名、不能排除记忆影响，通道与设置不同，未统一控制所有变量。官方没有逐项分数或年度第二第三名。详细界限见方法文档。

欢迎提交自己的复测报告，记录实际型号、日期、输入哈希、提示词、完整输出以及有无联网；不要上传没有再分发授权的照片或API密钥。

## 许可

MIT仅适用于本项目原创代码、提示词与说明，不覆盖摄影作品、官方输入说明或其他第三方材料。见[LICENSE](LICENSE)及[来源说明](docs/rights-and-sources.md)。
