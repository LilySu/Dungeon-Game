import React from 'react';
import PropTypes from 'prop-types';

//Similar to SignupForm.js

//ormally you’d want to collect more info on a user when they sign up 
//than you’d need when they log in (in fact, you can customize the 
//signup form if you like… Django’s User model supports email, 
//first_name, and last_name fields in addition to username and 
//password. Be sure to add the relevant fields to the serializer, 
//too, if you want the data back). Both components are stateful 
//to keep track of the data in their controlled inputs, and both 
//have handle_change() methods to adjust the component’s state 
//when the user types something into the form. Also, they both 
//receive a prop which dictates how the form should be processed
//upon submission.

class LoginForm extends React.Component {
  state = {
    username: '',
    password: ''
  };

  handle_change = e => {
    const name = e.target.name;
    const value = e.target.value;
    this.setState(prevstate => {
      const newState = { ...prevstate };
      newState[name] = value;
      return newState;
    });
  };

  render() {
    return (
      <form onSubmit={e => this.props.handle_login(e, this.state)}>
        <h4>Log In</h4>
        <label htmlFor="username">Username</label>
        <input
          type="text"
          name="username"
          value={this.state.username}
          onChange={this.handle_change}
        />
        <label htmlFor="password">Password</label>
        <input
          type="password"
          name="password"
          value={this.state.password}
          onChange={this.handle_change}
        />
        <input type="submit" />
      </form>
    );
  }
}

export default LoginForm;

LoginForm.propTypes = {
  handle_login: PropTypes.func.isRequired
};