import "./App.css";

import logo from "./logo.svg";

function MyTitle() {
  return <h1>Hello from my React Component</h1>;
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <MyTitle></MyTitle>
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
