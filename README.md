# GTIN-API for E-Commerce Integration README

## Introduction

Welcome to the documentation for the GTIN-13 API for E-Commerce Integration, a work-in-progress (WIP) project committed to facilitating seamless product listings on global e-commerce platforms like Bol.com and Amazon. As we journey towards becoming a certified GS1 Solution Provider, this project aims to generate GTIN-13 (formerly known as EAN-13) codes, the most commonly used GS1 product code, ensuring your products meet the global standard for identification and traceability.

### What is GTIN-13?

GTIN-13, the cornerstone of the GS1 system of standards, is a 13-digit number used to uniquely identify products at the item level in the retail sector. These identifiers are crucial for managing products in the supply chain, from the manufacturer to the consumer, ensuring compatibility and visibility across global markets and digital platforms.

## Utilizing the GTIN-13 API for E-Commerce Listings

This API serves as an invaluable tool for businesses aiming to streamline their online sales channels. By integrating with our GTIN-13 API, companies can automate the generation of global standard product identifiers, thereby simplifying the process of listing products on major e-commerce platforms such as Bol.com and Amazon.

### Technical Documentation: REST API Usage

Our RESTful API provides an intuitive interface for the asynchronous generation of GTIN-13 codes. Below, we detail the API's functionality, including request and response formats and guidelines for using the endpoints effectively.

### API Attribute Overview

* `accountNumber`: A 13-digit unique identifier assigned to each company registered with MijnGS1, provided by GS1 during the API subscription onboarding process. Format as a string.
* `status`: Indicate the product's status in Dutch: "Concept" (Draft), "Actief" (Active), or "Inactief" (Inactive). Transition only allowed from Concept to Actief or Actief to Inactief, not reversely. Format as a string.
* `gpc`: See below. Format as a string.
* `consumerUnit`: Indicate if the product is a consumer unit with "Ja" (Yes) or "Nee" (No) in Dutch. Format as a string.
* `packagingType`: Select a value from the packaging type list. See below. Format as a string.
* `targetMarketCountry`: The Dutch country name where the product will be sold. See below. Format as a string.
* `description`: A description of the product, limited to 300 characters. Format as a string.
* `language`: The language of the product description, to be provided in Dutch. See below. Format as a string.
* `brandName`: The brand name of the product, with a maximum of 70 characters. Format as a string.
* `subBrandName`: The sub-brand name, also limited to 70 characters. Format as a string.
* `netContent`: The numerical value representing the product's quantity. Format as an integer.
* `measurementUnit`: The unit of measurement, provided in Dutch. See below. Format as a string.
* `imageUrl`: A publicly accessible URL to an image of the product, preferably in a web-browser-friendly format such as JPG, PNG, or GIF. Format as a string.
* `contractNumber`: Located in MyGS1 (mijn.gs1.nl) under Company > Contracts. Format as a string.

### API Endpoints Overview

There are two primary endpoints in the API:

1. **GTIN-13 Generation Request Endpoint** - Initiates the GTIN-13 code generation process.
2. **Status & GTIN-13 Retrieval Endpoint** - Monitors the status of requests and retrieves generated GTIN-13 codes.

#### GTIN-13 Generation Request Endpoint

Submit your product details to this endpoint to generate GTIN-13 codes. The request supports batch operations:

```http
POST /api/gtin
```

```json
[
  {
    "accountNumber": "YourAccountNumber",
    "status": "active",
    "gpc": "Gastrointestinal Drugs - Other",
    "consumerUnit": "Yes",
    "packagingType": "Drum",
    "targetMarketCountry": "Global Market",
    "description": "Sample product",
    "language": "English",
    "brandName": "Brand sample",
    "subBrandName": "Sub brand name",
    "netContent": 100,
    "measurementUnit": "Pound (0.45359237 kg)",
    "imageUrl": "",
    "contractNumber": "YourContractNumber"
  }
]
```

Success responses (200 OK) include a `jobId` of the UUID format for precise tracking:

```json
{
  "jobId": "e0a953c3-ee58-4b05-9d1b-174509c4e4d7"
}
```

Invalid requests will return a 403.

#### Job Status & GTIN-13 Retrieval Endpoint

With the `jobId`, check the status and retrieve your GTIN-13 codes:

```http
GET /api/gtin/status/e0a953c3-ee58-4b05-9d1b-174509c4e4d7
```

The response includes the request status and the GTIN-13 details for each product:

```json
{
  "status": "processing",
  "results": [
    {
      "status": "done",
      "result": {
        "gtin": "1212323312345",
        "accountNumber": "YourAccountNumber",
        "description": "Sample product",
        "language": "English",
        "brandName": "Brand sample",
        // Additional fields as submitted
      }
    }
  ]
}
```

#### GTIN-13 Retrieval Endpoint

With the `gtin`, retrieve the details:

```http
GET /api/gtin/1212323312345
```

The response includes the request status and the GTIN-13 details for each product:

```json
{
    "gtin": "1212323312345",
    "accountNumber": "YourAccountNumber",
    "description": "Sample product",
    "language": "English",
    "brandName": "Brand sample",
    // Additional fields as submitted
}
```

### API options

#### Field Length Restrictions

Please note the following restrictions on field lengths when submitting your product information:

* `brandName` and `subBrandName`: Maximum of 70 characters
* `description`: Maximum of 300 characters

#### Packaging Type Options

The `packagingType` field.

Refer to the [packagingType.txt](./packagingType.txt) file for a complete list.

#### GPC Options

The `gpc` field. 

Use valid values from the GPC list available at [GPC Browser](https://gpc-browser.gs1.org/) (select Dutch).

Refer to the [gpc.txt](./gpc.txt) file for a complete list.

#### Language Options

The `language` field.

Refer to the [language.txt](./language.txt) file for a complete list.

#### Target Market Country Options

The `targetMarketCountry` field.

Refer to the [targetMarketCountry.txt](./targetMarketCountry.txt) file for a complete list.

#### Measure Unit Options

The `measurementUnit` field.

Refer to the [measurementUnit.txt](./measurementUnit.txt) file for a complete list.

### Leveraging GTIN-13 on E-Commerce Platforms

With the GTIN-13 codes generated through our API, businesses can efficiently list their products on platforms like Bol.com and Amazon, ensuring global reach and compliance with e-commerce standards. This streamlined approach facilitates quicker product uploads, enhanced market visibility, and adherence to international retail requirements.

## Conclusion

The GTIN-13 API for E-Commerce Integration offers a pivotal solution for businesses looking to expand their presence on major e-commerce platforms. As this project evolves, we remain committed to enhancing its capabilities and support for our users. For further assistance, please refer to our documentation or contact our support team.

Thank you for considering our GTIN-13 API for your e-commerce integration needs. We look forward to supporting your business's growth and success online.