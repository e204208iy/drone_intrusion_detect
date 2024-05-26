# 特定の領域への侵入検知
- メインのファイルがdetect_HArea.pyです。
　## 解説
- ultralytics.solutionsのobject_counterモデルの180行目で人が領域に入ったことを検知している。
- リストのself.in_polygonの中にTrueが入っている場合CV2でテキストをputするようにしている。
- 領域の設定をいじる場合はultralytics.utils.plottingのAnnotatorモデルのdraw_regionメソッドをいじる。
