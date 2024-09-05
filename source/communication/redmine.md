## Redmine編

### オープンにコミュニケーションをしよう
* 全員が全ての情報にアクセス出来るように権限を設定して、情報共有のコストを下げよう
* やってることを薄く、広く、常に共有しよう(Redmineではなくてもいいのでは？)
* お客さんも自分たちも一つのチームとしてコミュニケーションしよう

### タスクを依頼されたら、まずチケットを作る

* チケット作成を習慣づけましょう
  * 「必要ないチケット」を作ってしまったらクローズしたらいい。（コストが安い）
  * 「チケット作らず、タスクを忘れちゃった」 -> あとでフォローが大変（コストが高い） 

### 結果だけでなく、思考の過程や結果の理由をチケットに書く
* 同じ困ったことが起きたときに過去のナレッジから対処できるようになる
* レビューを見て、こう考えたからこうなんだとレビューする人が判断しやすい。（仕事のエビデンス）

### チケットの粒度を適切にする
* あまり大きすぎると進め方がわからなかったり分担ができない
* 適度にすると進んでる感が出る
* 仕事の見通しが悪くなる
* 小さすぎるとチケットを作るのが目的のようになる

### プロジェクトにあったテンプレート作ろう

* 雛形があると書き方について悩まず、要点だけでも投稿できる
* テンプレートは生き物。必要な時はテンプレートを更新しよう
* 新しくテンプレートが必要になったら、ほしい人が作成しよう
* こう書いて欲しい、というルールがあるなら、テンプレ化しよう（タイトルにこれを書いて、とか）

### チケットには担当者をつける

* 「誰」が、「何」を「いつまでに」するか、明確に記録しておこう
* 担当者がはっきりわかっていると、すぐに着手できる
* アサイン先候補が複数いる場合、botに `$choice`で選んでもらってアサインしましょう

### 担当者を変える際には担当者を明確にしよう

* Slackや口頭だけでは後から確認しづらいので、必ずチケットの注釈に依頼内容を書こう
* 依頼内容には「誰に」「何やってほしいか」をコメントで明確にして担当者を変えよう

### 作成者はチケットの終了条件を書く（ゴールを書く）
* ある「タスク」に対して、「アクション」が必要、その「アクション」の「結果」を記載する 
* 終了条件が決まっていると、仕事の意図が共有できて差し戻しが少なくなる

### チケットには期限を設定しよう

* 期限を設定するとbotが期限間近や期限切れになると教えてくれる
* 期限を過ぎたチケットをいつまでも放置しない
* いつかやるチケットは、きっとやらない

### チケットの本文を更新しよう

* チケット本文だけを見て必要な情報を理解できるようにしよう
* あとから終了したチケットをみたとき、本文だけでなにが起きたか分かると時間が節約できる
* チケットの本文に必要な情報がすべて書いてあると、コメントを追うことなく内容が理解できる

### Slackで議論したことを、まとめて起票する

* Slackは「流れていく」会話
* あとになって文脈がわからない、あとになって探すのは大変である
* 関連するチケットのコメントに、議論内容を残しましょう
* (わざわざSlackの記録を書き直す必要はない)

### 重要なチケットについては、チャットでメンションしよう

* すぐアクション、相談等が必要な内容はチャットでメンションしましよう

### チケットを閉じるのは作成者

* 作成者は、「あるタスク」にたいして、「あるアクション」を求め、「ある結果」を期待する
* そのため、「実際の結果」を確認するのは作成者である