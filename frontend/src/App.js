import { useState, useEffect, Component } from "react";
import axios from "axios";

export default function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios("https://teaminnovation-endpoint.herokuapp.com/eoi-list/")
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => console.error(`Error: ${error}`));
  }, []);

  console.log(data);

  return (
    <div>
      hello world
      {data.map((info) => (
        <p>{info.email}</p>
      ))}
    </div>
  );
}
