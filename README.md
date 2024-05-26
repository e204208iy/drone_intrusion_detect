# 特定の領域への侵入検知
- メインのファイルがdetect_HArea.pyです。
- YOLOv8に実装されているTrackモデルの機能を拡張して実装しています。
## 解説

### 処理の流れ
人間を検出する → BBOXの座標を取得 → 事前設定した領域の中にいるのか判定 → テキスト表示 → 最初に戻る
### 細かい設定
- ultralytics.solutionsのobject_counterモデルの180行目で人が領域に入ったことを検知している。
  - リストのself.in_polygonの中にTrueが入っている場合CV2でテキストをputするようにしている。
- 領域の設定をいじる場合はultralytics.utils.plottingのAnnotatorモデルのdraw_regionメソッドをいじる。

