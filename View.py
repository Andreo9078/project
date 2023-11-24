import dearpygui.dearpygui as dpg
import Presenter


class MainView:
    def __init__(self, app_name: str) -> None:
        dpg.create_context()

        self.presenter: Presenter.MainPresenter | None = None

        self.window = dpg.window
        self.font = None

        self._create_viewport(app_name, 600, 200)

    @staticmethod
    def _create_viewport(app_name: str,
                         width: int, height: int) -> None:
        dpg.create_viewport(title=app_name, width=width, height=height)
        dpg.setup_dearpygui()
        dpg.show_viewport()

    def set_font(self, font_src, font_name: str, size: int) -> None:
        with dpg.font_registry():
            with dpg.font(font_src, size, tag=font_name) as f:
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

        self.font = font_name

    @property
    def error_msg(self):
        return dpg.get_value("error")

    @error_msg.setter
    def error_msg(self, error: str) -> None:
        dpg.set_value("error", error)

    @property
    def result_msg(self) -> str:
        return dpg.get_value("result")

    @result_msg.setter
    def result_msg(self, result: str) -> None:
        dpg.set_value("result", result)

    @property
    def parameter(self) -> str:
        return dpg.get_value("parameters")

    @property
    def value(self) -> float:
        return dpg.get_value("value")

    def setup_window(self, window_name: str) -> None:
        with dpg.value_registry():
            dpg.add_string_value(tag="parameters")
            dpg.add_float_value(tag="value")
            dpg.add_string_value(tag="result")
            dpg.add_string_value(tag="error")

        with self.window(tag=window_name, width=600, height=200):
            dpg.add_text("Расчет параметров треугольника")
            dpg.add_combo(items=("Площадь", "Сторона", "Радиус вписанной окружности", "Радиус описанной окружности"),
                          label="Возможные параметры", source="parameters")
            dpg.add_input_float(default_value=0, width=100, label="Значение параметра", source="value")
            dpg.add_button(label="Вычислить", callback=self.presenter.result_button_clicked, user_data=dpg)

            dpg.add_text(source="result")
            dpg.add_text(source="error", color=(255, 20, 20))

        if self.font is not None:
            dpg.bind_font(self.font)

        dpg.set_primary_window(window_name, True)

    def set_presenter(self, presenter) -> None:
        self.presenter = presenter

    def start(self):
        if not isinstance(self.presenter, Presenter.MainPresenter):
            dpg.destroy_context()
            raise Exception("Presenter can`t be not MainPresenter type.\n"
                            "\t\t   Use set_presenter method to set presenter.")
        dpg.start_dearpygui()

    def __del__(self):
        dpg.destroy_context()
