# ghmo

通过 GitHub Actions 自动化导出 有关模型，比如MobileSAM 轻量化模型（.pt 转 .onnx），并自动发布到 GitHub Release，全程无需本地配置依赖，适配后续 Go + ONNX Runtime 竹签计数、实例分割等场景。

## 📌 项目核心目标 1
无需本地安装 Python、PyTorch 等依赖，通过 GitHub Actions 云端自动化完成：
- 自动下载 MobileSAM 官方 .pt 模型
- 将 .pt 模型导出为 CPU 可运行的 ONNX 轻量化模型（~10MB）
- 自动将 ONNX 模型发布到 GitHub Release，方便直接下载使用
- 适配后续 Go 项目（竹签实例分割、自动计数、描框+编号）

## 📋 目录结构
ghmo/
├── .github/
│   └── workflows/
│       └── build-mb-sam-onnx.yml  # 核心自动化工作流
└── README.md                   # 项目说明文档
