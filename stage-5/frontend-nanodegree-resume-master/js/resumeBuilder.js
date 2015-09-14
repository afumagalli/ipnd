var bio = {
	"name" : "Anthony Fumagalli",
	"role" : "Educator",
	"contact" : {
		"mobile" : "(619) 341-9571",
		"email" : "anthony.fumagalli@gmail.com",
		"github" : "afumagalli",
		"twitter" : "antfumagalli",
		"location" : "Mountain View, CA"
	},
	"picture" : "images/fry.jpg",
	"welcome" : "Welcome to my page!",
	"skills" : ["programming", "teaching"]
};

var formattedName = HTMLheaderName.replace("%data%", bio.name);
var formattedRole = HTMLheaderRole.replace("%data%", bio.role);

$("#header").prepend(formattedRole);
$("#header").prepend(formattedName);

var work = {
	"jobs" : [
		{
			"position" : "Course Manager",
			"employer" : "Udacity",
			"years" : "< 1",
			"city" : "Mountain View, CA"
		}
	}
}

var education = {
	"schools" : [
		{
			"name" : "Yale University",
			"years" : "2011 - 2015",
			"city" : "New Haven, CT",
			"major" : "Computer Science & Mathematics"
		},
		{
			"name" : "Crawford High School",
			"years" : "2007 - 2011",
			"city" : "San Diego, CA"
		}
	]
}

var projects = {
	"projects" : [
		{
			"title" : "Bash",
			"dates" : "November 2014",
			"description" : "A bash-like shell in C",
			"images" : []
		}
	]
}