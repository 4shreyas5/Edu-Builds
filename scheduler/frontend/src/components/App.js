import React, { Component } from 'react';
import { render } from 'react-dom';


export default class App extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (<h1>Hello, this is a react-project</h1>);
    }

}


// Place the component in html
const appDiv = document.getElementById("app");
render(<App />, appDiv);
