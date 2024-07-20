import React, { useEffect, useState } from 'react'; 
import Axios from 'axios'; 

function Display() {

    const [items, setItems] = useState(""); 

    const fetchData = () => {

        Axios.get('http://127.0.0.1:5000/api/items')
            .then(res => {
                setItems(res.data); 
                console.log(res.data); 
            }); 

    }

    useEffect(() => {
        fetchData(); 
    }, []);

    const RenderItems = () => {

        return(

            <ul>

                {Object.keys(items).map((item) => (
                    <li>
                        <div class="flex justify-between w-3/4 pl-10 pr-10 pt-5 pb-5">
                            <p>{item}</p>
                            <button>Test</button>  
                        </div>
                    </li>
                ))}

            </ul>

        );

    }

    return(

        <div className="flex justify-center ml-10 mr-10 mt-10">

            <div className="flex justify-between bg-white w-3/4 pl-10 pr-10 pt-5 pb-5 shadow-2xl">

                <RenderItems />

            </div>

        </div>

    );

}

export default Display; 