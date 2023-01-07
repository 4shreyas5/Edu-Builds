import React, { Component } from 'react';
import { render } from 'react-dom';


export default class App extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (<div>
            <form action='http://127.0.0.1:8000/api/form-submit/' method='POST'>
                <input name="course-name" type="text" placeholder='Course Name' required/>
                <input name="course-url" type="text" placeholder='Course URL' required/>
                <input name="course-duration" type="text" placeholder='Course duration' required/>
                <button type="submit">Submit here</button>
            </form>
        </div>);
    }

}


// Place the component in html
const appDiv = document.getElementById("app");
render(<App />, appDiv);
