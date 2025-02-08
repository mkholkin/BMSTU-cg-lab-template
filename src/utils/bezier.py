from typing import Sequence, Generator


class BezierCurve:
    def __init__(self, points: Sequence[Sequence[float]], ) -> None:
        self.points = points

    # TODO: Вынести в отдельно место?
    def lerp(self, p1: Sequence[float], p2: Sequence[float], t: float) -> tuple[float, float]:
        return p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t

    def __next_point(self, anchor_points: Sequence[Sequence[float]], t: float) -> tuple[float, float]:
        if len(anchor_points) == 2:
            return self.lerp(anchor_points[0], anchor_points[1], t)

        new_anchor_points = []
        for i in range(len(anchor_points) - 1):
            new_anchor_points.append(self.lerp(anchor_points[i], anchor_points[i + 1], t))

        return self.__next_point(new_anchor_points, t)

    def interpolate(self, npoints: int) -> Generator[tuple[float, float], int, None]:
        if npoints <= 2:
            raise ValueError("Number of points can't be less than 2")

        for i in range(npoints + 1):
            yield self.__next_point(self.points, i / npoints)
