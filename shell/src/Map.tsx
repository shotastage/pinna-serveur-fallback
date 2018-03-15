/*
PINNA
Map.tsx

Created by Shota Shimazu on 2018/03/05

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
*/

import * as React from 'react';
import './Map.css';

interface GoogleMapProps {}
interface GoogleMapState {
    map: google.maps.Map;
}

class Map extends React.Component<GoogleMapProps, GoogleMapState> {
   
    render() {
        return (
            <div className="Map">
                <header className="Map-header">
                    <h1 className="Map-title">PINNA</h1>
                </header>
                <p className="Map-intro">
                    To get started, edit <code>src/App.tsx</code> and save to reload.
                </p>
            </div>
        );
    }
}

export default Map;
