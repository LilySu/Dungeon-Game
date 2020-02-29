import React, { Component } from 'react';
import Nav from './components/Nav';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';
import './App.css';

//component’s state is initialized and the logged_in property is determined 
//based on whether or not a token can be found in local storage. 
class App extends Component {
  constructor(props) { 
    super(props);
    this.state = {
      displayed_form: '',
      logged_in: localStorage.getItem('token') ? true : false,
      username: ''
    };
  }

//if a token has been found, we make a request to the initialize() in adventure > api.py we defined in Django.
  componentDidMount() {
    if (this.state.logged_in) {
      fetch('http://localhost:8000/adventure/current_user/', {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`
        }
      })
        .then(res => res.json())
        .then(json => {
          this.setState({ username: json.username });
        });
    }
  }
//Notice that we specify the Authorization header in the format ‘JWT <token>’. Each request to the 
//API which requires the user to be authenticated will need to include this header, in this format, 
//in order for the request to be processed. Then, we parse the response as JSON, and add the 
//user’s username to the component’s state.



//we make a POST request to the obtain_jwt_token view that we tried out before… only this time, 
//because we changed the default response payload handler, the response from this viewpoint will 
//include the user’s serialized data along with the token. 
  handle_login = (e, data) => {
    e.preventDefault();
    fetch('http://localhost:8000/token-auth/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(json => {
        localStorage.setItem('token', json.token);
        this.setState({
          logged_in: true,
          displayed_form: '',
          username: json.user.username
        });
      });
  };



//makes a POST request to our UserList view, which also returns the user’s serialized data and 
//token. In both of these cases, the token is stored into local storage once the response has 
//been parsed into JSON. 
  handle_signup = (e, data) => {
    e.preventDefault();
    fetch('http://localhost:8000/adventure/users/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(json => {
        localStorage.setItem('token', json.token);
        this.setState({
          logged_in: true,
          displayed_form: '',
          username: json.username
        });
      });
  };

  //deletes the token from local storage (no request necessary).
  handle_logout = () => {
    localStorage.removeItem('token');
    this.setState({ logged_in: false, username: '' });
  };

  //handles the UI.
  display_form = form => {
    this.setState({
      displayed_form: form
    });
  };

//handles the UI.
  render() {
    let form;
    switch (this.state.displayed_form) {
      case 'login':
        form = <LoginForm handle_login={this.handle_login} />;
        break;
      case 'signup':
        form = <SignupForm handle_signup={this.handle_signup} />;
        break;
      default:
        form = null;
    }

    return (
      <div className="App">
        <Nav
          logged_in={this.state.logged_in}
          display_form={this.display_form}
          handle_logout={this.handle_logout}
        />
        {form}
        <h3>
          {this.state.logged_in
            ? `Hello, ${this.state.username}`
            : 'Please Log In'}
        </h3>
      </div>
    );
  }
}

export default App;