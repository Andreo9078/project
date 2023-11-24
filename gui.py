from Presenter import MainPresenter
from View import MainView
from triangle import EquilateralTriangle

view = MainView("App")
presenter = MainPresenter(EquilateralTriangle())
presenter.set_view(view)
view.set_presenter(presenter)
view.set_font("./fonts/arialmt.ttf", "default", 12)
view.setup_window("main")
view.start()