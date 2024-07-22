let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
  columnDefs: [
    { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6] },
    { orderable: false, targets: [5, 6] },
    { sercheable: false, targets: [1, 2, 3, 4] },
  ],
};

const initDataTable = async () => {
  if (dataTableIsInitialized) {
    dataTable.destroy();
  }
  await listProgrammers();

  dataTable = $("#datatable_programmers").DataTable(dataTableOptions);
  dataTableIsInitialized = true;
};

const listProgrammers = async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/app/list_programmers/");
    const data = await response.json();
    let content = "";
    data.programmers.forEach((programmer, index) => {
      content += `
                <tr>
                    <td>${index}</td>
                    <td>${programmer.name}</td>
                    <td>${programmer.country}</td>
                    <td>${programmer.contratado}</td>
                </tr>
            `;
    });
    tableBody_programmers.innerHTML = content;
  } catch (ex) {
    alert(ex);
  }
};

window.addEventListener("load", async () => {
  await initDataTable();
});
