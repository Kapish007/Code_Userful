# Code For Select 2 add(multipal options)

#Add script in heder
<link rel="stylesheet" href="{% static 'assets/select2.min.css' %}" />
#Add script in heder


#Add script in footer
<script src="{% static 'assets/select2.min.js' %}"></script>
or
  <script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/js/select2.min.js"></script>
#Add script in footer


# html div add select2 in class

<div class="form-group col-md-3">
											<label for="Quantities_Managed">Quantities Managed</label>
                                           <select name="Quantities_Managed" id="Quantities_Managed" class="form-control ms select2" data-placeholder="Select Quantities" multiple >
                                             
													
												 <option value="1 to 15 kg">1 to 15 kg</option> 
												<option value="15 to 50 kg">15 to 50 kg</option> 
													<option value="50 to 300 kg">50 to 300 kg</option>
													<option value="Above 300 kg">Above 300 kg</option>
													
														
												</select>
												<center><span style="display:none;color:red;font-size: 14px;" id ="Quantities_Managed_error">Please Enter Quantities Managed</span></center>
                                            </div>
                                            

# html div add select2 in class                                            






















# To Update and show selected value in form
	# // add multipal option from Quantities_Managed_arr
    # Quantities_Managed is list from python backend
		var Quantities_Managed_arr = []
		var Quantities_Managed_data = ""
		$('#Quantities_Managed').select2({
		closeOnSelect: true,
		multiple: true,
		placeholder: "Select Quantities"
		});
		console.log(Quantities_Managed_list)
		 for (i = 0; i < Quantities_Managed_list.length; i++){
			console.log(Quantities_Managed_list[i])
			Quantities_Managed_data = Quantities_Managed_list[i]
			Quantities_Managed_arr.push(Quantities_Managed_data.toString());}
		
		<!-- alert(arr) -->
		$("#Quantities_Managed").val(Quantities_Managed_arr);
		$('#Quantities_Managed').trigger('change');
		
		
		# // add multipal option from Quantities_Managed_arr








