# beproud-guide

* BeProudで生活するための手引き
* ここにはBeProudで生活するための手引きとなるスライドを置く予定です

## ライフスタイルガイド

* スライド: [BeProudライフスタイルガイド](https://gitpitch.com/beproud/beproud-guide?p=lifestyle)
* Markdown: [lifestyle/PITCHME.md](lifestyle/PITCHME.md)

## コミュニケーションガイド

* スライド: [BeProudコミュニケーションガイド](https://gitpitch.com/beproud/beproud-guide?p=communication)
* Markdown: [communication/PITCHME.md](communication/PITCHME.md)

## How to Contribute

* Pull Requestください。BPの中の人が誰かがレビューしてLGTMならmergeしてください。
* 対象ファイルは `lifestyle/` `communication/` 配下の `.md` ファイルです。
* [T.B.D] PRに書いてほしいこと

### GitPitchについて

* [GitPitch](https://gitpitch.com/)はMarkdownのドキュメントをスライドで表示するサービスです
* `PITCHEME.md` というMarkdownのドキュメントを変換してスライドで表示しています
* 基本的には以下の形式で1スライドを記述します(`---` がスライドの区切り)
  * 詳細な書き方は「参考」にあるドキュメントなどを参照してください

```markdown
---

## 1スライドのタイトル

* 箇条書きの説明
* 箇条書きの説明

--- 

## 次のスライドのタイトル

* 箇条書きの説明
  * インデントも普通にできる

```

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