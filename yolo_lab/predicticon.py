from cv2 import grabCut
from ultralytics import YOLO
from ultralytics.engine.results import Results


class GetPos:
    result: list[Results] | None = None  # 明确声明类型，而不是裸 None

    @classmethod
    def init(cls, source):
        yolo = YOLO("icon.pt", task="detect")
        # 图片
        cls.result = yolo(source=source, save=True)

    @classmethod
    def get_icon_id(cls, icon_name: str):
        if cls.result is None:
            raise RuntimeError("请先调用 GetPos.init()")
        for k, v in cls.result[0].names.items():
            if v == icon_name:
                return k

    @classmethod
    def get_cls_no(cls, icon_id: int):
        if cls.result is None:
            raise RuntimeError("请先调用 GetPos.init()")
        for k, v in enumerate(cls.result[0].boxes.cls):
            if v == icon_id:
                return k

    @classmethod
    def get_xy(cls, cls_no: int):
        if cls.result is None:
            raise RuntimeError("请先调用 GetPos.init()")
        x = cls.result[0].boxes.xywh[cls_no][0]
        y = cls.result[0].boxes.xywh[cls_no][1]
        return x, y

    @classmethod
    def get_pos(cls, icon_name):
        if cls.result is None:
            raise RuntimeError("请先调用 GetPos.init()")
        icon_id = cls.get_icon_id(icon_name)
        if icon_id is None:
            return
        cls_no = cls.get_cls_no(icon_id)
        if cls_no is None:
            return
        pos = cls.get_xy(cls_no)
        return pos


if __name__ == "__main__":
    GetPos.init("iconimg.png")
    print(GetPos.get_pos("garbage"))
