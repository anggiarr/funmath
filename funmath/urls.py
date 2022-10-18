
from django.contrib import admin
from django.urls import path
from beraksi.views import indexberaksi
from profildeveloper.views import indexprofildeveloper
from profildosen.views import indexprofildosen
from tentang.views import indextentang
from welcome.views import indexwelcome
from yukbermain.views import indexyukbermain
from petunjuk1.views import indexpetunjuk1
from submaterispldv.views import indexsubmaterispldv
from pengertianspldv.views import indexpengertianspldv
from sejarahspldv.views import indexsejarahspldv
from metodespldv.views import indexmetodespldv
from bagianspldv.views import indexbagianspldv
from hasilspldv.views import indexhasilspldv
from jenisspldv.views import indexjenisspldv
from langkahspldv.views import indexlangkahspldv
from submaterisptldv.views import indexsubmaterisptldv
from pengertiansptldv.views import indexpengertiansptldv
from sifatsptldv.views import indexsifatsptldv
from himpunansptldv.views import indexhimpunansptldv
from langkahsptldv.views import indexlangkahsptldv
from beraksispldv.views import indexberaksispldv
from beraksisptldv.views import indexberaksisptldv
from games.views import indexgames
from end.views import indexend
from highscores.views import indexhighscores

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', indexwelcome),
    path('profildeveloper/', indexprofildeveloper),
    path('profildosen/', indexprofildosen),
    path('tentang/', indextentang),
    path('yukbermain/', indexyukbermain),
    path('beraksi/', indexberaksi),
    path('petunjuk1/', indexpetunjuk1),
    path('submaterispldv/', indexsubmaterispldv),
    path('pengertianspldv/', indexpengertianspldv),
    path('sejarahspldv/', indexsejarahspldv),
    path('metodespldv/', indexmetodespldv),
    path('bagianspldv/', indexbagianspldv),
    path('hasilspldv/', indexhasilspldv),
    path('jenisspldv/', indexjenisspldv),
    path('langkahspldv/', indexlangkahspldv),
    path('submaterisptldv/', indexsubmaterisptldv),
    path('pengertiansptldv/', indexpengertiansptldv),
    path('sifatsptldv/', indexsifatsptldv),
    path('himpunansptldv/', indexhimpunansptldv),
    path('langkahsptldv/', indexlangkahsptldv),
    path('beraksispldv/', indexberaksispldv),
    path('beraksisptldv/', indexberaksisptldv),
    path('games/', indexgames),
    path('end/', indexend),
    path('highscores/', indexhighscores),
]
