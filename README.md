# ネットワーク学習ノート

ネットワークスペシャリスト試験（以降ネスペ）対策を兼ねたネットワーク技術学習ノート。ネスペの過去問などを題材として扱いながら、ネットワークについて体系的に学んでいく。

## 過去問

- `past-exams/`に、H21(2009)からR7(2025)のうち、コロナで試験が実施されなかったR2(2020)を除いた16年分の公式過去問を配置。
- `past-exams/download-nw-exams.ps1`は、公式サイトからの過去問一括ダウンロード用PowerShellスクリプト
- 試験は、すべて60点以上で合格

## AM対策カテゴリ

- 午前1：9:30-10:20の50分、多肢選択式、30問出題30問必須
- 午前2：10:50-11:30の40分、多肢選択式、25問出題25問必須

午前試験対策用の学習内容を、IPAの出題分野に沿ってカテゴリ別に整理する。

| No. | 日本語                       | Directory                                                                      |
| --: | ---------------------------- | ------------------------------------------------------------------------------ |
|  01 | 基礎理論                     | [`01-basic-theory`](AM/01-basic-theory/)                                       |
|  02 | アルゴリズムとプログラミング | [`02-algorithms-and-programming`](AM/02-algorithms-and-programming/)           |
|  03 | コンピュータ構成要素         | [`03-computer-components`](AM/03-computer-components/)                         |
|  04 | システム構成要素             | [`04-system-components`](AM/04-system-components/)                             |
|  05 | ソフトウェア                 | [`05-software`](AM/05-software/)                                               |
|  06 | ハードウェア                 | [`06-hardware`](AM/06-hardware/)                                               |
|  07 | ユーザインタフェース         | [`07-user-interface`](AM/07-user-interface/)                                   |
|  08 | 情報メディア                 | [`08-information-media`](AM/08-information-media/)                             |
|  09 | データベース                 | [`09-database`](AM/09-database/)                                               |
|  10 | ネットワーク                 | [`10-network`](AM/10-network/)                                                 |
|  11 | セキュリティ                 | [`11-security`](AM/11-security/)                                               |
|  12 | システム開発技術             | [`12-system-development`](AM/12-system-development/)                           |
|  13 | ソフトウェア開発管理技術     | [`13-software-development-management`](AM/13-software-development-management/) |
|  14 | プロジェクトマネジメント     | [`14-project-management`](AM/14-project-management/)                           |
|  15 | サービスマネジメント         | [`15-service-management`](AM/15-service-management/)                           |
|  16 | システム監査                 | [`16-system-audit`](AM/16-system-audit/)                                       |
|  17 | システム戦略                 | [`17-system-strategy`](AM/17-system-strategy/)                                 |
|  18 | システム企画                 | [`18-system-planning`](AM/18-system-planning/)                                 |
|  19 | 経営戦略マネジメント         | [`19-business-strategy-management`](AM/19-business-strategy-management/)       |
|  20 | 技術戦略マネジメント         | [`20-technology-strategy-management`](AM/20-technology-strategy-management/)   |
|  21 | ビジネスインダストリ         | [`21-business-and-industry`](AM/21-business-and-industry/)                     |
|  22 | 企業活動                     | [`22-corporate-activities`](AM/22-corporate-activities/)                       |
|  23 | 法務                         | [`23-legal-affairs`](AM/23-legal-affairs/)                                     |

- NWでは、午前1は全分野から、午前2では、3,4,10,11,12,13から出題される。
- 11のセキュリティは、どの試験区分でも午前1,2共に頻出
- NWの午前2では、10,11が頻出
- 午前1は、どの分野からも満遍なく出題されるので、浅く広く勉強しておく必要がある。
- 午前試験では、過去問からの再利用が積極的にされている。全体的には、2-4年前の過去問が多く出題される傾向がある。

## AM対策ノート一覧

### 01 基礎理論

- [1-1 離散数学](AM/01-basic-theory/1-1-離散数学.md)
- [1-2 応用数学](AM/01-basic-theory/1-2-応用数学.md)
- [1-3 情報に関する理論](AM/01-basic-theory/1-3-情報に関する理論.md)
- [1-4 通信に関する理論](AM/01-basic-theory/1-4-通信に関する理論.md)

### 02 アルゴリズムとプログラミング

- [2-1 データ構造](AM/02-algorithms-and-programming/2-1-データ構造.md)
- [2-2 アルゴリズム](AM/02-algorithms-and-programming/2-2-アルゴリズム.md)
- [2-3 プログラム言語](AM/02-algorithms-and-programming/2-3-プログラム言語.md)

### 03 コンピュータ構成要素

- [3-1 プロセッサ](AM/03-computer-components/3-1-プロセッサ.md)
- [3-2 メモリ](AM/03-computer-components/3-2-メモリ.md)
- [3-3 バス](AM/03-computer-components/3-3-バス.md)
- [3-4 入出力デバイス](AM/03-computer-components/3-4-入出力デバイス.md)
- [3-5 入出力装置](AM/03-computer-components/3-5-入出力装置.md)

### 04 システム構成要素

- [4-1 システムの構成](AM/04-system-components/4-1-システムの構成.md)
- [4-2 システムの評価指標](AM/04-system-components/4-2-システムの評価指標.md)

### 05 ソフトウェア

- [5-1 オペレーティングシステム](AM/05-software/5-1-オペレーティングシステム.md)
- [5-2 ミドルウェア](AM/05-software/5-2-ミドルウェア.md)
- [5-3 ファイルシステム](AM/05-software/5-3-ファイルシステム.md)
- [5-4 開発ツール](AM/05-software/5-4-開発ツール.md)
- [5-5 オープンソースソフトウェア](AM/05-software/5-5-オープンソースソフトウェア.md)

### 06 ハードウェア

- [6-1 ハードウェア](AM/06-hardware/6-1-ハードウェア.md)

### 07 ユーザインタフェース

- [7-1 ユーザインタフェース](AM/07-user-interface/7-1-ユーザインタフェース.md)
- [7-2 UX-UI-デザイン](AM/07-user-interface/7-2-UX-UI-デザイン.md)

### 08 情報メディア

- [8-1 マルチメディア技術](AM/08-information-media/8-1-マルチメディア技術.md)
- [8-2 マルチメディア応用](AM/08-information-media/8-2-マルチメディア応用.md)

### 09 データベース

- [9-1 データベース方式](AM/09-database/9-1-データベース方式.md)
- [9-2 データベース設計](AM/09-database/9-2-データベース設計.md)
- [9-3 データ操作](AM/09-database/9-3-データ操作.md)
- [9-4 トランザクション処理](AM/09-database/9-4-トランザクション処理.md)
- [9-5 データベース応用](AM/09-database/9-5-データベース応用.md)

### 10 ネットワーク

- [10-1 ネットワーク方式](AM/10-network/10-1-ネットワーク方式.md)
- [10-2 データ通信と制御](AM/10-network/10-2-データ通信と制御.md)
- [10-3 通信プロトコル](AM/10-network/10-3-通信プロトコル.md)
- [10-4 ネットワーク管理](AM/10-network/10-4-ネットワーク管理.md)
- [10-5 ネットワーク応用](AM/10-network/10-5-ネットワーク応用.md)

### 11 セキュリティ

- [11-1 情報セキュリティ](AM/11-security/11-1-情報セキュリティ.md)
- [11-2 情報セキュリティ管理](AM/11-security/11-2-情報セキュリティ管理.md)
- [11-3 セキュリティ技術評価](AM/11-security/11-3-セキュリティ技術評価.md)
- [11-4 情報セキュリティ対策](AM/11-security/11-4-情報セキュリティ対策.md)
- [11-5 セキュリティ実装技術](AM/11-security/11-5-セキュリティ実装技術.md)

### 12 システム開発技術

- [12-1 システム-ソフトウェア-要件定義](AM/12-system-development/12-1-システム-ソフトウェア-要件定義.md)
- [12-2 設計](AM/12-system-development/12-2-設計.md)
- [12-3 実装-構築](AM/12-system-development/12-3-実装-構築.md)
- [12-4 統合-テスト](AM/12-system-development/12-4-統合-テスト.md)
- [12-5 導入-受け入れ支援](AM/12-system-development/12-5-導入-受け入れ支援.md)
- [12-6 保守-廃棄](AM/12-system-development/12-6-保守-廃棄.md)

### 13 ソフトウェア開発管理技術

- [13-1 開発プロセス-手法](AM/13-software-development-management/13-1-開発プロセス-手法.md)
- [13-2 知的財産適用管理](AM/13-software-development-management/13-2-知的財産適用管理.md)
- [13-3 開発環境管理](AM/13-software-development-management/13-3-開発環境管理.md)
- [13-4 構成管理-変更管理](AM/13-software-development-management/13-4-構成管理-変更管理.md)

### 14 プロジェクトマネジメント

- [14-1 プロジェクトマネジメント](AM/14-project-management/14-1-プロジェクトマネジメント.md)
- [14-2 プロジェクトの統合](AM/14-project-management/14-2-プロジェクトの統合.md)
- [14-3 プロジェクトのステークホルダ](AM/14-project-management/14-3-プロジェクトのステークホルダ.md)
- [14-4 プロジェクトのスコープ](AM/14-project-management/14-4-プロジェクトのスコープ.md)
- [14-5 プロジェクトの資源](AM/14-project-management/14-5-プロジェクトの資源.md)
- [14-6 プロジェクトの時間](AM/14-project-management/14-6-プロジェクトの時間.md)
- [14-7 プロジェクトのコスト](AM/14-project-management/14-7-プロジェクトのコスト.md)
- [14-8 プロジェクトのリスク](AM/14-project-management/14-8-プロジェクトのリスク.md)
- [14-9 プロジェクトの品質](AM/14-project-management/14-9-プロジェクトの品質.md)
- [14-10 プロジェクトの調達](AM/14-project-management/14-10-プロジェクトの調達.md)
- [14-11 プロジェクトのコミュニケーション](AM/14-project-management/14-11-プロジェクトのコミュニケーション.md)

### 15 サービスマネジメント

- [15-1 サービスマネジメント](AM/15-service-management/15-1-サービスマネジメント.md)
- [15-2 サービスマネジメントシステムの計画及び運用](AM/15-service-management/15-2-サービスマネジメントシステムの計画及び運用.md)
- [15-3 パフォーマンス評価及び改善](AM/15-service-management/15-3-パフォーマンス評価及び改善.md)
- [15-4 サービスの運用](AM/15-service-management/15-4-サービスの運用.md)
- [15-5 ファシリティマネジメント](AM/15-service-management/15-5-ファシリティマネジメント.md)

### 16 システム監査

- [16-1 システム監査](AM/16-system-audit/16-1-システム監査.md)
- [16-2 内部統制](AM/16-system-audit/16-2-内部統制.md)

### 17 システム戦略

- [17-1 情報システム戦略](AM/17-system-strategy/17-1-情報システム戦略.md)
- [17-2 業務プロセス](AM/17-system-strategy/17-2-業務プロセス.md)
- [17-3 ソリューションビジネス](AM/17-system-strategy/17-3-ソリューションビジネス.md)
- [17-4 システム活用促進及び評価](AM/17-system-strategy/17-4-システム活用促進及び評価.md)

### 18 システム企画

- [18-1 システム化計画](AM/18-system-planning/18-1-システム化計画.md)
- [18-2 要件定義](AM/18-system-planning/18-2-要件定義.md)
- [18-3 調達計画及び実施](AM/18-system-planning/18-3-調達計画及び実施.md)

### 19 経営戦略マネジメント

- [19-1 経営戦略手法](AM/19-business-strategy-management/19-1-経営戦略手法.md)
- [19-2 マーケティング](AM/19-business-strategy-management/19-2-マーケティング.md)
- [19-3 ビジネス戦略と目標及び評価](AM/19-business-strategy-management/19-3-ビジネス戦略と目標及び評価.md)
- [19-4 経営管理システム](AM/19-business-strategy-management/19-4-経営管理システム.md)

### 20 技術戦略マネジメント

- [20-1 技術開発戦略の立案](AM/20-technology-strategy-management/20-1-技術開発戦略の立案.md)

### 21 ビジネスインダストリ

- [21-1 ビジネスシステム](AM/21-business-and-industry/21-1-ビジネスシステム.md)
- [21-2 エンジニアリングシステム](AM/21-business-and-industry/21-2-エンジニアリングシステム.md)
- [21-3 eビジネス](AM/21-business-and-industry/21-3-eビジネス.md)
- [21-4 民生機器](AM/21-business-and-industry/21-4-民生機器.md)
- [21-5 産業機器](AM/21-business-and-industry/21-5-産業機器.md)

### 22 企業活動

- [22-1 経営-組織論](AM/22-corporate-activities/22-1-経営-組織論.md)
- [22-2 業務分析-データ利活用](AM/22-corporate-activities/22-2-業務分析-データ利活用.md)
- [22-3 会計-財務](AM/22-corporate-activities/22-3-会計-財務.md)

### 23 法務

- [23-1 知的財産権](AM/23-legal-affairs/23-1-知的財産権.md)
- [23-2 セキュリティ関連法規](AM/23-legal-affairs/23-2-セキュリティ関連法規.md)
- [23-3 労働関連-取引関連法規](AM/23-legal-affairs/23-3-労働関連-取引関連法規.md)
- [23-4 その他の法律-ガイドライン-技術者倫理](AM/23-legal-affairs/23-4-その他の法律-ガイドライン-技術者倫理.md)

## 午後対策

- 午後1：12:30-14:00の90分、記述式、3問出題2問解答
- 午後2：14:30-16:30の120分、記述式、2問出題1問解答