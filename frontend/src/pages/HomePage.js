import { useState, useEffect } from "react";
import axios from "axios";

function HomePage() {
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
        <p key={info.id}>{info.email}</p>
      ))}
    </div>
  );
}

export default HomePage;
