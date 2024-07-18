import React, { useEffect } from 'react'; 

function Enter() {

    useEffect(() => {
        const item = document.getElementById("item"); 
        const priority = document.getElementById("priority");
        const handleKeyDown = (e) => {
            if (e.key === "Enter") {
                console.log(item.value); 
                console.log(priority.value);
            }

            // Send data to Flask backend using fetch
            fetch('/input', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ item: item.value, priority: priority.value }),
            })
            .then(response => response.json())
            .then(data => {
                console.log(data.message); 
            })
            .catch(error => {
                console.error('There was an error writing the priority!', error);
            });
        };

        priority.addEventListener("keydown", handleKeyDown);

        // Clean up event listener on component unmount
        return () => {
            priority.removeEventListener("keydown", handleKeyDown);
        };

    }, []);

    return(

        <div className="flex justify-center ml-10 mr-10">

            <div className="flex justify-between bg-white w-3/4 pl-10 pr-10 pt-5 pb-5">

                {/* to-do item details */}
                <form className="flex justify-start items-center w-3/4">
                    <label className="mr-4 font-bold">Enter Item:</label>
                    <input id="item" type="text" maxLength="50" autoComplete="off" className="rounded-lg pl-2 pr-2 w-3/4"></input>
                </form>

                {/* to-do item priority */}
                <form className="flex justify-end items-center w-1/4">
                    <label className="mr-4 font-bold">Priority:</label>
                    <input id="priority" type="number" min="1" autoComplete="off" className="rounded-lg pl-2 pr-2 w-20"></input>
                </form>

            </div>

        </div>

    );

}

export default Enter; 