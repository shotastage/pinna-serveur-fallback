/*
 PINNA Shell
 index.ts

 Created by Shota Shimazu on 2018/2/14

 Copyright (c) 2018 Shota Shimazu All Rights Reserved.

 This software is released under the terms of PINNA Software License, see LICENSE for detail.
 https://github.com/shotastage/pinna-music/blob/master/LICENSE
*/

import * as React from 'react';
import * as ReactDOM from 'react-dom';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import './index.css';

ReactDOM.render(
  <App />,
  document.getElementById('root') as HTMLElement
);
registerServiceWorker();
