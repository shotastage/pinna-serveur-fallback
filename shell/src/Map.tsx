/// <reference path="../node_modules/@types/googlemaps/index.d.ts"/>

/*
PINNA
Map.tsx

Created by Shota Shimazu on 2018/03/05

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
*/

import * as React from 'react';
import * as ReactDOM from "react-dom";
import './Map.css';


interface GoogleMapProps { }
interface GoogleMapState {
    map: google.maps.Map;
}

class Map extends React.Component<GoogleMapProps, GoogleMapState> {
   
    render() {
        if (this.state.map) {
            return (
                <div>
                    <div ref="top" style={{ height: 500 }}>
                        {this.props.children}
                    </div>
                </div>
            );
        } else {
            return (
                <div>
                    <div ref="top" style={{ height: 500 }}>
                    </div>
                </div>
            );
        }
    }

}

export default Map;
