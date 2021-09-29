# beproud-guide

* BeProudで生活するための手引き
* ここにはBeProudで生活するための手引きとなるスライドを置く予定です

## ライフスタイルガイド

* スライド: [BeProudライフスタイルガイド](https://beproud-guide.netlify.app/slides/lifestyle/) ([HTML版](https://beproud-guide.netlify.app/lifestyle/index.html))
* Markdown: [lifestyle/index.md](lifestyle/index.md)

## コミュニケーションガイド

* スライド: [BeProudコミュニケーションガイド](https://beproud-guide.netlify.app/slides/communication/) ([HTML版](https://beproud-guide.netlify.app/communication/index.html))
* Markdown: [communication/](communication/)

## How to Contribute

* Pull Requestください。BPの中の人が誰かがレビューしてLGTMならmergeしてください。
* 対象ファイルは `lifestyle/` `communication/` 配下の `.md` ファイルです。
* [T.B.D] PRに書いてほしいこと

### 考え方（レビュー観点）

* 大切なことが他にもあれば、追加しよう。場合によっては、分離しよう。
* 優先度の高いものを上にあげよう。優先度の低いものを下に下げよう。
* 細かすぎること、大切じゃないものは削除、マージしよう。
* 一枚のスライドで主張は一つにまとめよう。
* 具体的な行動につながるような書き方にしよう。
* 多すぎると読まないので、簡潔に書こう。
* スライドだけで伝わるようにしよう。説明なしで伝わるようにしよう。

## 参考

* [ダイヤモンドメディア サバイバルジャーニーガイド](https://www.slideshare.net/kozotakei/ss-81102661)
* #63314: ビープラウドのサバイバルジャーニーガイド、コミュニケーションガイドのスライド作る

## 環境構築

```bash
$ python3.9 -m venv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ make revealjs
(env) $ open _build/revealjs/index.html
```