---
status: published
published: true
title: Embedding Graphics in Jaspersoft Report Files
modified: '2018-12-31T21:13:40-05:00'
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 26977
wordpress_url: http://dltj.org/?p=26977
date: 2015-12-30 12:27:54 -0500
date_gmt: 2015-12-30 17:27:54 -0500
category: Raw Technology
categories:
- Raw Technology
tags:
- CollectionSpace
- JasperReports
- Jaspersoft Studio
comments:
- id: 687038
  author: Joe
  author_email: taepoop12@gmail.com
  author_url: ''
  date: 2017-01-06 00:49:51 -0500
  date_gmt: 2017-01-06 05:49:51 -0500
  content: "when i started to paste \r\n\r\nit gives me an error:\r\n\"The method decodeBase64(byte[]) is underfined for the type Base64"
- id: 687039
  author: Joe
  author_email: taepoop12@gmail.com
  author_url: ''
  date: 2017-01-06 00:50:42 -0500
  date_gmt: 2017-01-06 05:50:42 -0500
  content: "\"\"\r\nthis is what i paste when i am getting the error, STEP 4"
- id: 687040
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: 2017-01-06 15:18:15 -0500
  date_gmt: 2017-01-06 20:18:15 -0500
  content: I'm not seeing your entire message, I think.  You might try using a service list gist.github.com to post the details of the error you are seeing.  I haven't looked at this in a while, but as far as I know nothing extra is needed to include the Base64 classes in Jaspersoft.
- id: 688212
  author: Dawei
  author_email: riodavid@hotmail.com
  author_url: ''
  date: 2017-08-30 03:54:47 -0400
  date_gmt: 2017-08-30 07:54:47 -0400
  content: This is a very good one. But unfortunately if we download it into excel, the pictures are gone.
- id: 688706
  author: Marc Schambers
  author_email: marcschambers6@gmail.com
  author_url: http://www.TeamADR.com
  date: 2017-12-01 14:26:20 -0500
  date_gmt: 2017-12-01 19:26:20 -0500
  content: "Hi Joe,\r\nI had the exact same error.  I moved the statement, in the 'Source' tag, to below the grouping of property names and it worked:\r\n \t\r\n\t\r\n\t\r\n\t\r\n\t\r\n\r\nAlso, I changed the Evaluation Time to 'Report' on the image properties screen.  (Weird that after that change, is when it worked.  Setting it back to Report, works now too.)"
- id: 688707
  author: Marc Schambers
  author_email: marcschambers6@gmail.com
  author_url: http://www.TeamADR.com
  date: 2017-12-01 14:28:13 -0500
  date_gmt: 2017-12-01 19:28:13 -0500
  content: Make that change back to 'Now' :-)
- id: 688708
  author: Marc Schambers
  author_email: marcschambers6@gmail.com
  author_url: http://www.TeamADR.com
  date: 2017-12-01 14:33:59 -0500
  date_gmt: 2017-12-01 19:33:59 -0500
  content: "Hello Dawei,\r\nBy moving the -import- tag, I successfully imported the image into both .xls and .xlsx.  Give it a try and let me know if it works for you."
- id: 688722
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: 2017-12-06 11:09:50 -0500
  date_gmt: 2017-12-06 16:09:50 -0500
  content: Awesome!  Thanks for sharing your experience, Marc.
---
One of the features of [Jaspersoft Reports](http://www.jaspersoft.com/reporting-software "Reporting Software - TIBCO Jaspersoft") is the ability to include static graphics -- logos, for instance -- in the completed reports. These graphic files are normally listed in the JRXML configuration file by reference -- meaning that what is stored in the configuration is a file name and not the graphic itself. Most times the configuration file and the ancillary graphics files are uploaded to a JasperReports Server for execution. In the environment that I'm working in, [CollectionSpace](http://collectionspace.org/ "http://collectionspace.org/"), the report generator is embedded in the application without the JasperReports Server endpoint. The JRXML files must be compiled into the application, which makes keeping track of the ancillary graphics files somewhat troublesome.

Ideally, I would like to embed the graphics into the JRXML file itself, similar to what is done in with the [data URI schema in HTML and CSS files](https://en.wikipedia.org/wiki/Data_URI_scheme "Data URI Schema - Wikipedia") to reduce the connection latency between client and server. This is possible, but the instructions and hints you find out on the internet to do it are out of date or incomplete. The instructions below are correct for Jaspersoft Studio version 6.2.0.

## Step 1: Encode your image in base64

Base64 is a way to take a binary file and encode it into ASCII characters. XML files have limits on what they can contain, so encoding the binary image file in base64 provides a way to embed the image data into XML while still honoring the ASCII nature of XML. There are many ways to do the encoding; I use the [Base64 Image Encoder](https://www.base64-image.de/) site. What you will get back is a string of data that starts like this:

```plaintext
data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAY...
```

This is a DATA URI, and it contains details at the start that are not part of the image data itself. Everything up to and including the comma -- `data:image/jpeg;base64,` -- needs to be removed. The remainder of the string is the base64-encoded image data.

## Step 2: Put the base64 image data into a report variable
{{ image(width="300", localsrc="2015/12/1-add_variable-300x205.png", caption="In the Outline, right click on Variables to create a variable.") }}
To put the image data into the JRXML file, we will create a variable in the report. Right click (or control click) on the "Variables" heading in the Outline view, and select "Create Variable".  

{{ image(width="300", localsrc="2015/12/2-Properties_view-300x275.png", caption="Give the variable a name and paste the image data into the Expressions field in quotes.") }}
Give the variable a name and paste the image data into the Expressions field surrounded by double quotes. Leave all of the other values the same (Value Class Name is `java.lang.String`, no calculation function or increment type, reset type is `Report`, and no data in Initial Value Expression or Incrementer Factory Class Name).

## Step 3: Add image to the report
{{ image(width="300", localsrc="2015/12/3-Create_new_image_element-300x300.png", caption="Select 'Custom expression' and paste Java snippet.") }}

Click and drag an image element from the Palette onto the report. A "Create new image element" dialog box pops up with several choices for "Image creation mode", including a workspace resource, an absolute path, or a URL. Pick the last choice, "Custom expression", and enter this snippet of Java below. There is a place in the snippet where the variable with the base64-encoded image is included (`CSpaceLogo` in this case); replace this with the variable name from the previous step.

```java
new ByteArrayInputStream(Base64.decodeBase64($V{CSpaceLogo}.getBytes()))
```

## Step 4: Add Base64 class import to the report

One final step...in order to use the `Base64.decodeBase64` function when the report is run, we need to explicitly import that class when the report is run. In the report editor there are tabs for "Design", "Source", and "Preview". Click on "Source" to see the raw JRXML. Below the last line that starts with `<property name="</code">` and above the `<querystring>` line, add this line:

```xml
<import value="org.apache.commons.codec.binary.Base64"></import>
```

All done! Save and preview your report, and you'll see the image included in the report.
