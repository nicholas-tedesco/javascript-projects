import React, { useEffect, useState } from 'react'; 
import Axios from 'axios'; 

function Display() {

    // fetch to-do items from db 
    const [items, setItems] = useState(""); 

    const fetchData = () => {

        Axios.get('http://127.0.0.1:5000/api/items')
            .then(res => {
                var data = res.data; 
                setItems(data); 
                console.log(data); 
            }); 

    }

    useEffect(() => {
        fetchData(); 
    }, []);

    // delete record if user clicks 
    const deleteRecord = (priority) => {

        var delete_url = 'http://127.0.0.1:5000/api/delete/' + priority;
        console.log(delete_url);

        Axios.delete(delete_url)
            .then(res => console.log(res)); 

        window.location.reload();

    }

    const RenderItems = () => {

        return(

            <div className="ml-10 mr-10 mt-10">

                {Object.keys(items).map((item) => (

                    <div className="flex justify-center">

                        <div className="flex justify-between items-center bg-white w-3/4 pl-10 pr-10 pt-5 pb-5 shadow-2xl">
                        
                                {/* to-do item details */}
                                <p>{item}</p>

                            {/* option to remove */}
                            <button onClick={() => deleteRecord(items[item])} className="focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-900">Complete</button>

                        </div>

                    </div>

                ))}

            </div>

        );

    }

    return(

        <div>
            <RenderItems />
        </div>

    );

}

export default Display; 