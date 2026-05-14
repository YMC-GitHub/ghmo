import torch
import onnx
import onnxsim
from mobile_sam import sam_model_registry

# 加载模型
model = sam_model_registry["vit_t"](checkpoint="../weights/mobile_sam.pt")
model.eval()

# 构造输入
dummy_input = torch.randn(1, 3, 640, 640)

# 导出 ONNX
torch.onnx.export(
    model,
    dummy_input,
    "mobile_sam.onnx",
    opset_version=17,
    input_names=["image"],
    output_names=["masks", "iou_predictions"],
    do_constant_folding=True
)

# 简化模型
model_onnx = onnx.load("mobile_sam.onnx")
model_onnx, check = onnxsim.simplify(model_onnx)
onnx.save(model_onnx, "mobile_sam.onnx")