# to save image using ajax




function fin(){
debugger;
var name = $("#Name_user").val();
		var Shop_Name = $('#Shop_Name').val();
		var Address = $('#Address').val();
		var address_textarea = $('#address_textarea').val();
		var PAN_Number = $('#PAN_Number').val();
		var Aadhar_Number = $('#Aadhar_Number').val();
		var Pincode = $('#Pincode').val();
		<!-- var WCheck_box = document.getElementById("WCheck_box"); -->
		var ID = $('#ID').val();
		var Opening_Time = $('#Opening_Time').val();
		var Closing_Time = $('#Closing_Time').val();
		var Pick_up = document.getElementById("Pick_up");
		var Drop_off = document.getElementById("Drop_off");
		
		var Bank_Name = $('#Bank_Name').val();
		var Account_Number = $('#Account_Number').val();
		var Phone = $('#Phone').val();
		var GST_Number = $('#GST_Number').val();
		var Collection_Partner = $('#Collection_Partner').val();
		var Company_Type = $('#Company_Type').val();
		var pick_latitude = document.getElementById("pick_latitude").value
		var pick_longitude = document.getElementById("pick_longitude").value
 

		
        if (Pick_up.checked == true){
    var Pick_up_v = "ON"
  } else {
    var Pick_up_v = "OFF"
  }
  if (Drop_off.checked == true){
    var Drop_off_v = "ON"
  } else {
    var Drop_off_v = "OFF"
  }
  <!-- if (WCheck_box.checked == true){ -->
    <!-- var WCheck_box_v = "ON" -->
  <!-- } else { -->
    <!-- var WCheck_box_v = "OFF" -->
  <!-- } -->
       
 
 
 
 
	if (name == ""){
		$('#nema_error').show();
	}
	else if (Shop_Name == ""){
		$('#Shop_Name_error').show();
		
	}
	
	else if (address_textarea == ""){
		$('#Shop_Address_error').show();
	}
	else if (Address == ""){$('#Geolocation_error').show();	}
	else if (Pincode == ""){$('#pin_code_error').show();	}
	else if (Opening_Time == ""){$('#Opening_Time_error').show();	}
	else if (Closing_Time == ""){$('#Closing_Time_error').show();	}
	
	else if (Bank_Name == ""){$('#Bank_Name_error').show();	}
	else if (Account_Number == ""){$('#Account_Number_error').show();	}
	else if (GST_Number == ""){$('#GST_Number_error').show();}
	else if (PAN_Number == ""){$('#PAN_Number_error').show();}
	else if (Aadhar_Number == ""){$('#Aadhar_Number_error').show();}
	else if (Phone == ""){$('#Phone_error').show();	}
	
	else{
  var Material_selected = [];
  for (var option of document.getElementById('Material_deals_list').options) {
    if (option.selected) {
      Material_selected.push(option.value);
    }
  }
  var Quantities_Managed = [];
  for (var option of document.getElementById('Quantities_Managed').options) {
    if (option.selected) {
      Quantities_Managed.push(option.value);
    }
  }
  console.log(Quantities_Managed)
  var Open_Days = [];
  for (var option of document.getElementById('Open_Days').options) {
    if (option.selected) {
      Open_Days.push(option.value);
    }
  }
  console.log(Open_Days)
  //Drop off Items Accepted
  
  var Drop_off_Items_Accepted = [];
  for (var option of document.getElementById('Drop_off_Items_Accepted').options) {
    if (option.selected) {
      Drop_off_Items_Accepted.push(option.value);
    }
  }
  console.log(Drop_off_Items_Accepted)
  
  
  
  
		var form = $('form_data')[0];
		var formData = new FormData(form);
		formData.append('Image', document.getElementById('Image').files[0]);
		formData.append('PAN_Card', document.getElementById('PAN_Card').files[0]);
		formData.append('Aadhar_Card', document.getElementById('Aadhar_Card').files[0]);
		formData.append('GST_doc', document.getElementById('GST_doc').files[0]);
		formData.append("Name",name);
		formData.append("Address",Address);
		formData.append("pick_latitude",pick_latitude);
		formData.append("pick_longitude",pick_longitude);
		formData.append("Pincode",Pincode);
		formData.append("Phone",Phone);
		<!-- formData.append("WCheck_box",WCheck_box_v); -->
		formData.append("Shop_Name",Shop_Name);
		formData.append("ID",ID);
		formData.append("Quantities_Managed",JSON.stringify(Quantities_Managed));
		formData.append("GST_Number",GST_Number);
		formData.append("Bank_Name",Bank_Name);
		formData.append("Account_Number",Account_Number);
		formData.append('Material_deals_list', JSON.stringify(Material_selected));
		formData.append('Open_Days', JSON.stringify(Open_Days));
		formData.append("Opening_Time",Opening_Time);
		formData.append("Closing_Time",Closing_Time);
		formData.append("Pick_up",Pick_up_v);
		formData.append("Drop_off",Drop_off_v);
		formData.append("Collection_Partner",Collection_Partner);
		formData.append("Company_Type",Company_Type);
		formData.append("address_textarea",address_textarea);
		formData.append("PAN_Number",PAN_Number);
		formData.append("Aadhar_Number",Aadhar_Number);
		formData.append("Drop_off_Items_Accepted",JSON.stringify(Drop_off_Items_Accepted));
  
  
  
  
  
  
  
  $.ajax({
                        method : "POST",
						url : "/add_representative/",
						enctype : "mutipart/form_data",
						processData : false,
						contentType : false,
						cache : false,
						data : formData,
						success : function(response){
							
				
								<!-- $("#table_show").html(""); -->
                                <!-- $("#table_show").html(response); -->
									location.reload();
								
							
							
								
						}
						
                    })
					<!-- $(".step1").show(); -->
            <!-- $(".step2").hide(); -->
  
  }
  
  
  
  
}