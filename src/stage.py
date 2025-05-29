from src.block import Block


class Stage:
    @staticmethod
    def load_stage():
        return [Stage.stage1(), Stage.stage2()]

    @staticmethod
    def stage1():
        blocks = []
        for y in range(4):
            for x in range(10):
                blocks.append(Block(x * 80 + 10, y * 30 + 10))
        return blocks

    @staticmethod
    def stage2():
        blocks = []
        for y in range(3):
            for x in range(5):
                blocks.append(Block(x * 160 + 30, y * 40 + 100))
        return blocks
