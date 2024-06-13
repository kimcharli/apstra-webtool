import React, { useState, useRef } from "react";
import Papa from "papaparse";
import { socket, socketEnum } from "../socket";
import "./GenericSystem.css";


const Ids = Object.freeze({
    GS_TABLE: "gs-table",
    BTN_PARSE: "parse-csv",
    TBL_HEADER: "table-header",
    TBL_BODY: "table-body",
});

// put this out of the GenericSystem component. Otherwise, it may trigger twice
socket.on(socketEnum.GS_SAMPLE, (data) => {
    console.log("socket.on(GS_SAMPLE)", data);
    const element = document.createElement('a');
    const file = new Blob([data.file_content], {type: 'text/csv'});
    element.href = URL.createObjectURL(file);
    element.download = 'gs_sample.csv';
    // document.body.appendChild(element);
    element.click();
});


const GenericSystem = () => {
 
    // This state will store the parsed data
    const [data, setData] = useState([]);
 
    // It state will contain the error when
    // correct file extension is not used
    const [error, setError] = useState("");
 
    // It will store the file uploaded by the user
    const [file, setFile] = useState("");

    // const uploadRef = useRef(null);
    // const parseRef = useRef(null);

    // const gsTable = document.getElementById(Ids.GS_TABLE);
    // const parseButton = document.getElementById(Ids.BTN_PARSE);

    // This function will be called when
    // the file input changes
    const handleFileChange = (e) => {
        setError("");
 
        // Check if user has entered the file
        if (e.target.files.length) {
            const inputFile = e.target.files[0];
  
            // If input type is correct set the state
            setFile(inputFile);
            console.log(inputFile, file);
        }
        // document.getElementById(Ids.BTN_PARSE).click();
        // parseButton.click();
        // gsTable.deleteTHead();
        // parseRef.current.click();
    };


    const createDataElement = (htmlTag, innerText, idParent) => { 
        // console.log("createDataElement", htmlTag, innerText, idParent);
        let node = document.createElement(htmlTag); 
        let textnode = document.createTextNode(innerText); 
        node.appendChild(textnode); 
        document.getElementById(idParent).appendChild(node); 
    }

    const createHeaderElement = (columnText) => {
        // console.log("createHeaderElement", columnText);
        createDataElement("th", columnText, Ids.TBL_HEADER); 
    }

    const createCellData= (rowIndex, cellKey, cellText) => { 
        // console.log("createCellData", rowIndex, cellKey, cellText);
        if(cellKey === 'blueprint') { 
            let node = document.createElement("tr"); 
            node.setAttribute("id", "row" + rowIndex); 
            document.getElementById(Ids.TBL_BODY).appendChild(node);
        }
        createDataElement("td", cellText, "row" + rowIndex); 
    }

    const requestSample = async () => {
        socket.emit(socketEnum.GS_SAMPLE, {});
    };

 


    const handleParse = (e) => {
     
        console.log("handleParse begin", e, file);
        // If user clicks the parse button without
        // a file we show a error
        if (!file) return alert("Enter a valid file");
 
        // uploadRef.current.click();
        // Initialize a reader which allows user
        // to read any file or blob.
        const reader = new FileReader();
 
        console.log("handleParse reader", reader, "reader.readyState:", reader.readyState);
        // Event listener on reader when the file
        // loads, we parse it and set the data.
        reader.onload = async ({ target }) => {
            // console.log("reader.onload", target);
            const csv = Papa.parse(target.result, {
                header: true,
                complete: (results) => {
                    // render header 
                    results.meta.fields.forEach((header) => {
                        createHeaderElement(header);
                    });
                    // iterate each row
                    results.data.forEach((row, row_index) => {
                        // iterate each cell (column)
                        for (var key in row) {
                            createCellData(row_index, key, row[key]);
                        }
                    });  
                }

            });
            // wait for the csv to be parsed
            csv?.data;
        };
        console.log("post reader.onload", reader, reader.readyState);
        reader.readAsText(file);
    };
 
    return (
        <div className="gs-box">
            <h3>Generic Systems</h3>
            <input
                onChange={handleFileChange}
                id="csvInput"
                name="file"
                type="file"
                accept=".csv"
                // ref={uploadRef}
                // hidden
            />
            <div>
                {/* <a href="/gs_sample" download="gs_sample.csv">Download Sample</a> */}
                <button id="gs_sample" onClick={requestSample}>
                    Download CSV Sample
                </button>
                <button id={Ids.BTN_PARSE} onClick={handleParse}>
                    Parse CSV
                </button>
            </div>
            <table id={Ids.GS_TABLE}>
            <thead>
                <tr id={Ids.TBL_HEADER}></tr>
            </thead>
            <tbody id={Ids.TBL_BODY}></tbody>
            </table>
        </div>        
    );
};



export default GenericSystem;