import justpy as jp


class DefaultLayout(jp.QLayout):
    def __init__(self, view='hHh lpR fFf', **kwargs):
        super().__init__(view=view, **kwargs)

        qheader = jp.QHeader(
            a=self,
            classes="bg-primary text-white"
        )

        qtoolbar = jp.QToolbar(
            a=qheader
        )

        qdrawer = jp.QDrawer(
            a=self,
            show_if_above=True,
            v_mode="left",
            side="left",
            bordered=True
        )

        qscroll = jp.QScrollArea(
            a=qdrawer,
            classes="fit"
        )
        qlist = jp.QList(
            a=qscroll
        )
        a_classes = "p-2 m-2 hover:text-blue-400"
        jp.A(
            a=qlist,
            text="Home",
            href="/home",
            classes=a_classes
        )
        jp.Br(a=qlist)
        jp.A(
            a=qlist,
            text="About",
            href="/about",
            classes=a_classes
        )
        jp.Br(a=qlist)
        jp.A(
            a=qlist,
            text="Dictionary",
            href="/dictionary",
            classes=a_classes
        )

        jp.QBtn(
            a=qtoolbar,
            dense=True,
            flat=True,
            round=True,
            icon="menu",
            click=self.move_drawer,
            drawer=qdrawer
        )

        jp.QToolbarTitle(
            a=qtoolbar,
            text="Instant Dictionary"
        )

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
