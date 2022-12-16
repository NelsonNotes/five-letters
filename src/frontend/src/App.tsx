import { useState } from "react";
import gameLogo from "./assets/logo.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <div>
        <a href="#">
          <img src={gameLogo} className="logo react" alt="Game logo" />
        </a>
      </div>
      <h1>Игра в разработке</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          Вы накликали {count} раз
        </button>
      </div>
      <p className="read-the-docs">Пока можно потыкать счетчик</p>
    </div>
  );
}

export default App;
