function confirmDelete(codigo) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
          confirmButton: 'btn btn-success',
          cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
      })
      
      swalWithBootstrapButtons.fire({
        title: 'Estás seguro?',
        text: "No podras deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Si, Eliminalo!',
        cancelButtonText: 'No, Cancelalo!',
        reverseButtons: true
      }).then((result) => {
        if (result.isConfirmed) {
          alert(1)
          swalWithBootstrapButtons.fire(
            'Eliminado',
            'Tu archivo ha sido eliminado.',
            'success'
          ).then(function() {
            window.location.href = "/eliminar_producto/"+ codigo +"/";
        })
        } else if (
          /* Read more about handling dismissals below */
          result.dismiss === Swal.DismissReason.cancel
        ) {
          swalWithBootstrapButtons.fire(
            'Cancelado',
            'Tu archivo imaginario esta seguro uwu',
            'error'
          )
        }
      })
}