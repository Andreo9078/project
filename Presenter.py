import View
from triangle import EquilateralTriangle


class MainPresenter:
    def __init__(self, triangle: EquilateralTriangle) -> None:
        self.triangle = triangle
        self.view: View.MainView | None = None

    def set_view(self, view: View.MainView) -> None:
        self.view = view

    def _drop_result(self):
        res = (f"\nРезультат вычислений: \n"
               f"Площадь: {round(self.triangle.area, 3)}\n"
               f"Сторона: {round(self.triangle.side, 3)}\n"
               f"Радиус вписанной окружности треугольника: {round(self.triangle.r_inscribed_circle, 3)}\n"
               f"Радиус описанной окружности треугольника: {round(self.triangle.r_circumscribed_circle, 3)}\n")

        self.view.result_msg = res

    def result_button_clicked(self):
        self.view.error_msg = ""
        self.view.result_msg = ""

        if self.view.parameter == "":
            self.view.error_msg = "Вы не выбрали параметр"
        elif self.view.value <= 0:
            self.view.error_msg = "Значение параметра должно быть положительным числом"
        else:
            if self.view.parameter == "Площадь":
                self.triangle.area = self.view.value
                self._drop_result()
            elif self.view.parameter == "Сторона":
                self.triangle.side = self.view.value
                self._drop_result()
            elif self.view.parameter == "Радиус вписанной окружности":
                self.triangle.r_inscribed_circle = self.view.value
                self._drop_result()
            elif self.view.parameter == "Радиус описанной окружности":
                self.triangle.r_circumscribed_circle = self.view.value
                self._drop_result()

