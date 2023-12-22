# Shortest-Path-Search
# Customizable Route Visualizer

This Python script visualizes bike routes and calculates the shortest path between two points using OpenStreetMap data via the OSMnx library. It's initially set to Ariake, Japan, but can be easily customized for any location and preference.

## Key Features

- **Flexible Location**: Set the script to visualize networks in any location.
- **Diverse Network Types**: Work with different types of routes including bike, walk, and drive.
- **Custom Route Calculation**: Uses Dijkstra's algorithm for path finding, which can be adjusted or replaced.
- **Interactive Visualization**: Leverages Matplotlib for detailed and customizable visual output.

## Customization Guide

1. **Change Location**: Replace `"Ariake, Japan"` with your desired place name in the `place_name` variable.
2. **Adjust Network Type**: Change `'bike'` in `network_type='bike'` to another type like `'walk'` or `'drive'`.
3. **Set Start and End Points**: Modify coordinates in `orig` and `dest` with your preferred longitude and latitude.
4. **Customize Path Finding**: Alter the `dijkstra` function or use a different algorithm from NetworkX.
5. **Adjust Visualization**: Customize plotting settings like colors and line widths in the Matplotlib functions.

## Getting Started

- **Install Python and Libraries**: Ensure Python is installed along with osmnx, networkx, matplotlib, shapely, and geopandas.
- **Download and Modify**: Download the script, make your customizations, and run it in your environment.
- **Explore**: Experiment with different settings to explore various routes and networks.

## Note

This script is for educational and planning purposes and should not be solely relied upon for precise navigation.
-----------------------------------------------------------------------------------------------------------------
# 可定制的路线可视化工具

此 Python 脚本可视化自行车路线，并通过 OSMnx 库使用 OpenStreetMap 数据计算两点之间的最短路径。 它最初设置为日本有明，但可以根据任何位置和偏好轻松定制。

＃＃ 主要特征

- **灵活位置**：设置脚本以可视化任何位置的网络。
- **多样化的网络类型**：使用不同类型的路线，包括自行车、步行和驾车。
- **自定义路线计算**：使用Dijkstra算法进行寻路，可以调整或替换。
- **交互式可视化**：利用 Matplotlib 提供详细且可定制的视觉输出。

## 定制指南

1. **更改位置**：将 `place_name` 变量中的 `"Ariake, Japan"` 替换为您想要的地名。
2. **调整网络类型**：将`network_type='bike'`中的`'bike'`更改为其他类型，例如`'walk'`或`'drive'`。
3. **设置起点和终点**：用您喜欢的经度和纬度修改“orig”和“dest”中的坐标。
4. **自定义路径查找**：更改 `dijkstra` 函数或使用与 NetworkX 不同的算法。
5. **调整可视化**：自定义绘图设置，例如 Matplotlib 函数中的颜色和线宽。

＃＃ 入门

- **安装 Python 和库**：确保 Python 与 osmnx、networkx、matplotlib、shapely 和 geopandas 一起安装。
- **下载和修改**：下载脚本，进行自定义，然后在您的环境中运行它。
- **探索**：尝试不同的设置来探索各种路线和网络。

＃＃ 笔记

该脚本用于教育和规划目的，不应仅依赖于精确导航。
-----------------------------------------------------------------------------------------------------------------

# カスタマイズ可能なルートビジュアライザー

この Python スクリプトは、自転車ルートを視覚化し、OSMnx ライブラリ経由で OpenStreetMap データを使用して 2 点間の最短経路を計算します。 最初は日本の有明に設定されていますが、場所や好みに合わせて簡単にカスタマイズできます。

## 主な機能

- **柔軟な場所**: スクリプトを設定して、任意の場所のネットワークを視覚化します。
- **多様なネットワーク タイプ**: 自転車、徒歩、車などのさまざまなタイプのルートを操作します。
- **カスタム ルート計算**: 経路検索にダイクストラのアルゴリズムを使用します。これは調整または置換できます。
- **インタラクティブな視覚化**: Matplotlib を活用して、詳細でカスタマイズ可能な視覚的な出力を実現します。

## カスタマイズガイド

1. **場所の変更**: `place_name` 変数の `"Ariake, Japan"` を希望の場所の名前に置き換えます。
2. **ネットワーク タイプを調整**: `network_type='bike'` の `'bike'` を `'walk'` や `'drive'` などの別のタイプに変更します。
3. **開始点と終了点の設定**: `orig` と `dest` の座標を好みの経度と緯度で変更します。
4. **パス検索をカスタマイズ**: 「dijkstra」関数を変更するか、NetworkX とは異なるアルゴリズムを使用します。
5. **視覚化の調整**: Matplotlib 関数で色や線幅などのプロット設定をカスタマイズします。

＃＃ はじめる

- **Python とライブラリをインストール**: Python が osmnx、networkx、matplotlib、shapely、および geopandas とともにインストールされていることを確認します。
- **ダウンロードして変更**: スクリプトをダウンロードし、カスタマイズして、環境で実行します。
- **探索**: さまざまな設定を試して、さまざまなルートとネットワークを探索します。

＃＃ 注記

このスクリプトは教育と計画を目的としており、正確なナビゲーションのみに依存すべきではありません。
