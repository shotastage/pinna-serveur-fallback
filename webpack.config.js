//
// PINNA Shell
// webpack.config.js
//
// Created by Shota Shimazu on 2018/2/14
//
// Copyright (c) 2018 Shota Shimazu All Rights Reserved.
//
// This software is released under the terms of PINNA Software License, see LICENSE for detail.
// https://github.com/shotastage/pinna-music/blob/master/LICENSE
//

module.exports = {
    entry: "./shell/src/index.tsx",
    output: {
        filename: "bundle.js",
        path: __dirname + "/shell/dist"
    },
    // Enable sourcemaps for debugging webpack's output.
    devtool: "source-map",
  
    resolve: {
        // Add '.ts' and '.tsx' as resolvable extensions.
        extensions: [".ts", ".tsx", ".js", ".json"]
    },
    module: {
        rules: [
            // All files with a '.ts' or '.tsx' extension will be handled by 'awesome-typescript-loader'.
            { test: /\.tsx?$/, loader: "awesome-typescript-loader" },
  
            // All output '.js' files will have any sourcemaps re-processed by 'source-map-loader'.
            { enforce: "pre", test: /\.js$/, loader: "source-map-loader" }
        ]
    },  
};
