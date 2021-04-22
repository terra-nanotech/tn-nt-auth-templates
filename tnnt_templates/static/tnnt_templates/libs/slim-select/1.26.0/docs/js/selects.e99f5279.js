(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["selects"],{"0047":function(e,t,a){"use strict";var s=a("5b19"),n=a.n(s);n.a},"5b19":function(e,t,a){},"60e0":function(e,t,a){"use strict";a.r(t);var s=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{attrs:{id:"selects-content"}},[a("div",{staticClass:"content"},[a("h2",{staticClass:"header"},[e._v("Single")]),a("p",[e._v(" Basic single select usage with Slim Select is extremely easy. Just set the select value to your select element. ")]),a("div",{staticClass:"select-split"},[a("div",[a("h4",[e._v("Options")]),a("select",{attrs:{id:"single"}},e._l(e.states,(function(t){return a("option",{key:t.abv,domProps:{value:t.abv,selected:t.selected}},[e._v(e._s(t.state))])})),0)]),a("div",[a("h4",[e._v("Optgroups")]),a("select",{attrs:{id:"single-group"}},e._l(e.foods,(function(t){return a("optgroup",{key:t.label,attrs:{label:t.label}},e._l(t.options,(function(t){return a("option",{key:t,domProps:{value:t}},[e._v(e._s(t))])})),0)})),0)])]),e._m(0),e._m(1)]),a("div",{staticClass:"content"},[a("h2",{staticClass:"header"},[e._v("Multiple")]),a("p",[e._v(" Multi selects work just the same as a single select. The only difference is setting the multiple attribute on your select. ")]),a("div",{staticClass:"select-split"},[a("div",[a("h4",[e._v("Options")]),a("select",{attrs:{id:"multiple",multiple:""}},e._l(e.states,(function(t){return a("option",{key:t.abv,domProps:{value:t.abv,selected:t.selected}},[e._v(e._s(t.state))])})),0)]),a("div",[a("h4",[e._v("Optgroups")]),a("select",{attrs:{id:"multiple-group",multiple:""}},e._l(e.foods,(function(t){return a("optgroup",{key:t.label,attrs:{label:t.label}},e._l(t.options,(function(t){return a("option",{key:t,domProps:{value:t}},[e._v(e._s(t))])})),0)})),0)])]),e._m(2),e._m(3)])])},n=[function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("pre",[e._v("      "),a("code",{staticClass:"language-javascript"},[e._v("\n        new SlimSelect({\n          select: '#single'\n        })\n      ")]),e._v("\n    ")])},function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("pre",[e._v("      "),a("code",{staticClass:"language-html"},[e._v('\n        \x3c!-- Options --\x3e\n        <select id="single">\n          <option value="value 1">Value 1</option>\n          <option value="value 2">Value 2</option>\n          <option value="value 3">Value 3</option>\n        </select>\n\n        \x3c!-- Optgroups --\x3e\n        <select id="single-optgroups">\n          <optgroup label="Label 1">\n            <option value="value 1">Value 1</option>\n            <option value="value 2">Value 2</option>\n            <option value="value 3">Value 3</option>\n          </optgroup>\n          <optgroup label="Label 2">\n            <option value="value 21">Value 1</option>\n            <option value="value 22">Value 2</option>\n            <option value="value 23">Value 3</option>\n          </optgroup>\n        </select>\n      ')]),e._v("\n    ")])},function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("pre",[e._v("      "),a("code",{staticClass:"language-javascript"},[e._v("\n        new SlimSelect({\n          select: '#multiple'\n        })\n      ")]),e._v("\n    ")])},function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("pre",[e._v("      "),a("code",{staticClass:"language-html"},[e._v('\n        \x3c!-- Options --\x3e\n        <select id="multiple" multiple>\n          <option value="value 1">Value 1</option>\n          <option value="value 2">Value 2</option>\n          <option value="value 3">Value 3</option>\n        </select>\n\n        \x3c!-- Optgroups --\x3e\n        <select id="multiple-optgroups" multiple>\n          <optgroup label="Label 1">\n            <option value="value 1">Value 1</option>\n            <option value="value 2">Value 2</option>\n            <option value="value 3">Value 3</option>\n          </optgroup>\n          <optgroup label="Label 2">\n            <option value="value 21">Value 1</option>\n            <option value="value 22">Value 2</option>\n            <option value="value 23">Value 3</option>\n          </optgroup>\n        </select>\n      ')]),e._v("\n    ")])}],l=a("2b0e"),o=a("ba4b"),i=l["a"].extend({data:function(){return{states:[{abv:"AL",state:"Alabama"},{abv:"AK",state:"Alaska"},{abv:"AZ",state:"Arizona"},{abv:"AR",state:"Arkansas"},{abv:"CA",state:"California",selected:!0},{abv:"CO",state:"Colorado"},{abv:"CT",state:"Connecticut"},{abv:"DE",state:"Delaware"},{abv:"DC",state:"District Of Columbia"},{abv:"FL",state:"Florida"},{abv:"GA",state:"Georgia"},{abv:"HI",state:"Hawaii"},{abv:"ID",state:"Idaho"},{abv:"IL",state:"Illinois",selected:!0},{abv:"IN",state:"Indiana"},{abv:"IA",state:"Iowa"},{abv:"KS",state:"Kansas"},{abv:"KY",state:"Kentucky"},{abv:"LA",state:"Louisiana"},{abv:"ME",state:"Maine"},{abv:"MD",state:"Maryland"},{abv:"MA",state:"Massachusetts"},{abv:"MI",state:"Michigan"},{abv:"MN",state:"Minnesota"},{abv:"MS",state:"Mississippi"},{abv:"MO",state:"Missouri"},{abv:"MT",state:"Montana"},{abv:"NE",state:"Nebraska"},{abv:"NV",state:"Nevada"},{abv:"NH",state:"New Hampshire"},{abv:"NJ",state:"New Jersey"},{abv:"NM",state:"New Mexico"},{abv:"NY",state:"New York"},{abv:"NC",state:"North Carolina"},{abv:"ND",state:"North Dakota"},{abv:"OH",state:"Ohio"},{abv:"OK",state:"Oklahoma"},{abv:"OR",state:"Oregon"},{abv:"PA",state:"Pennsylvania"},{abv:"RI",state:"Rhode Island"},{abv:"SC",state:"South Carolina"},{abv:"SD",state:"South Dakota"},{abv:"TN",state:"Tennessee"},{abv:"TX",state:"Texas"},{abv:"UT",state:"Utah"},{abv:"VT",state:"Vermont"},{abv:"VA",state:"Virginia"},{abv:"WA",state:"Washington"},{abv:"WV",state:"West Virginia"},{abv:"WI",state:"Wisconsin"},{abv:"WY",state:"Wyoming"}],foods:[{label:"Dairy",options:["Milk","Cheese","Butter","Ice Cream"]},{label:"Meat",options:["Beef","Ham","Pork","Sausage","Chicken","Turkey"]},{label:"Fruits",options:["Apple","Banana","Grape","Orange","Strawberry","Blueberry","Raspberry"]},{label:"Vegetables",options:["Carrot","Tomato","Broccoli","Celery","Corn","Pumpkin","Kale","Spinach"]}]}},mounted:function(){new o["a"]({select:"#single"}),new o["a"]({select:"#single-group"}),new o["a"]({select:"#multiple"});var e=new o["a"]({select:"#multiple-group"});e.set(["Cheese","Apple","Corn"])}}),u=i,v=(a("0047"),a("2877")),p=Object(v["a"])(u,s,n,!1,null,null,null);t["default"]=p.exports}}]);
//# sourceMappingURL=selects.e99f5279.js.map
