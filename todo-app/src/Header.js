import checklist from './checklist.png';

function Header() {
    return(

        <header className="flex justify-center ml-10 mr-10 mt-20">
            <div className="flex justify-between pl-10 pr-10 pt-8 pb-5 rounded-t-3xl w-3/4 bg-white shadow-2xl">

                {/* header text */}
                <div className="flex-col justify-center">
                    <div className="flex justify-start">
                        <h1 className="font-bold text-2xl">My To-Do List</h1>
                    </div>
                    <div className="mt-2 flex justify-start">
                        <p>a shitty app made by</p>
                        &nbsp; 
                        <p className="text-blue-600">Nick Tedesco</p>
                    </div>
                </div>

                {/* header icon */}
                <img src={checklist} width="60px" />

            </div>
        </header>

    );
}

export default Header; 