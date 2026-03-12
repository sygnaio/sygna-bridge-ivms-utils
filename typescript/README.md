# Sygna Bridge IVMS Util For Javascript
[<img src="https://img.shields.io/github/package-json/v/sygnaio/sygna-bridge-ivms-utils/master/typescript?style=for-the-badge">](https://www.npmjs.com/package/@sygna/bridge-ivms-util)

## Installation
```
npm install @sygna/bridge-ivms-util
```

## Example

### Legacy Version

```javascript
const ivms = require("@sygna/bridge-ivms-util");

// Originator
// originator name id
const orgNameId = new ivms.legacy.NaturalPersonNameId();
orgNameId.setPrimaryIdentifier("Wu");
orgNameId.setSecondaryIdentifier("Xinli");
orgNameId.setNameIdentifierType(
  ivms.legacy.NaturalPersonNameIdNameIdentifierTypeEnum.LEGL
);

// another name id for originator
const orgNameIdLocal = new ivms.legacy.LocalNaturalPersonNameId();
orgNameIdLocal.setPrimaryIdentifier("吳");
orgNameIdLocal.setSecondaryIdentifier("信利");
orgNameIdLocal.setNameIdentifierType(
  ivms.legacy.LocalNaturalPersonNameIdNameIdentifierTypeEnum.LEGL
);

// assign two name id to originator name
const orgPersonName = new ivms.legacy.NaturalPersonName();
orgPersonName.setNameIdentifiers([orgNameId]);
orgPersonName.setLocalNameIdentifiers([orgNameIdLocal]);

// originator national id and data
const orgPersonNationalId = new ivms.legacy.NationalIdentification();
orgPersonNationalId.setNationalIdentifier("446005");
orgPersonNationalId.setNationalIdentifierType(
  ivms.legacy.NationalIdentificationNationalIdentifierTypeEnum.RAID
);
orgPersonNationalId.setRegistrationAuthority("RA000553");

// assign name, national id, country to originator natural person
const originatingNaturalPerson = new ivms.legacy.NaturalPerson();
originatingNaturalPerson.setName(orgPersonName);
originatingNaturalPerson.setNationalIdentification(orgPersonNationalId);
originatingNaturalPerson.setCountryOfResidence("TZ");

// assign originator to person object
const originatingPerson = new ivms.legacy.Person();
originatingPerson.setNaturalPerson(originatingNaturalPerson);

// assign originator person and account id to originator
const originator = new ivms.legacy.Originator();
originator.setOriginatorPersons([originatingPerson]);
originator.setAccountNumbers(["1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"]);

// Beneficiary
// beneficiary 1 name id
const bene1NameId = new ivms.legacy.LegalPersonNameId();
bene1NameId.setLegalPersonName("ABC Limited");
bene1NameId.setLegalPersonNameIdentifierType(
  ivms.legacy.LegalPersonNameIdLegalPersonNameIdentifierTypeEnum.LEGL
);

// assign beneficiary 1 name with id
const bene1PersonName = new ivms.legacy.LegalPersonName();
bene1PersonName.setNameIdentifiers([bene1NameId]);

// beneficiary 1 is a legal person
const beneficiary1LegalPerson = new ivms.legacy.LegalPerson();
beneficiary1LegalPerson.setName(bene1PersonName);

// assign beneficiary 1 to person object
const beneficiary1Person = new ivms.legacy.Person();
beneficiary1Person.setLegalPerson(beneficiary1LegalPerson);

// beneficiary 2 name id
const bene2NameId = new ivms.legacy.LegalPersonNameId();
bene2NameId.setLegalPersonName("CBA Trading");
bene2NameId.setLegalPersonNameIdentifierType(
  ivms.legacy.LegalPersonNameIdLegalPersonNameIdentifierTypeEnum.TRAD
);

// assign beneficiary 2 name with id
const bene2PersonName = new ivms.legacy.LegalPersonName();
bene2PersonName.setNameIdentifiers([bene2NameId]);

// beneficiary 2 is a legal person
const beneficiary2LegalPerson = new ivms.legacy.LegalPerson();
beneficiary2LegalPerson.setName(bene2PersonName);

// assign beneficiary 2 to person object
const beneficiary2Person = new ivms.legacy.Person();
beneficiary2Person.setLegalPerson(beneficiary2LegalPerson);

// assign both persons to beneficiary object
const beneficiary = new ivms.legacy.Beneficiary();
beneficiary.setBeneficiaryPersons([beneficiary1Person, beneficiary2Person]);

// assign originator and beneficiary data to identity payload
const privateInfo = new ivms.legacy.IdentityPayload();
privateInfo.setOriginator(originator);
privateInfo.setBeneficiary(beneficiary);

const jsonData = privateInfo.serializeToJson();
console.log(JSON.stringify(jsonData, null, 2));

// decode from json data
const decoded = ivms.legacy.IdentityPayload.deserilizeFromJson(jsonData);
console.log(JSON.stringify(decoded.serializeToJson(), null, 2));
```

### IVMS2023 Version

```javascript
const ivms = require("@sygna/bridge-ivms-util");

// Originator
// originator name id
const orgNameId = new ivms.ivms2023.NaturalPersonNameId();
orgNameId.setPrimaryIdentifier("Wu");
orgNameId.setSecondaryIdentifier("Xinli");
orgNameId.setNameIdentifierType(
  ivms.ivms2023.NaturalPersonNameIdNameIdentifierTypeEnum.LEGL
);

// another name id for originator
const orgNameIdLocal = new ivms.ivms2023.LocalNaturalPersonNameId();
orgNameIdLocal.setPrimaryIdentifier("吳");
orgNameIdLocal.setSecondaryIdentifier("信利");
orgNameIdLocal.setNameIdentifierType(
  ivms.ivms2023.LocalNaturalPersonNameIdNameIdentifierTypeEnum.LEGL
);

// assign two name id to originator name
const orgPersonName = new ivms.ivms2023.NaturalPersonName();
orgPersonName.setNameIdentifier([orgNameId]);
orgPersonName.setLocalNameIdentifier([orgNameIdLocal]);

// originator national id and data
const orgPersonNationalId = new ivms.ivms2023.NationalIdentification();
orgPersonNationalId.setNationalIdentifier("446005");
orgPersonNationalId.setNationalIdentifierType(
  ivms.ivms2023.NationalIdentificationNationalIdentifierTypeEnum.RAID
);
orgPersonNationalId.setRegistrationAuthority("RA000553");

// assign name, national id, country to originator natural person
const originatingNaturalPerson = new ivms.ivms2023.NaturalPerson();
originatingNaturalPerson.setName(orgPersonName);
originatingNaturalPerson.setNationalIdentification(orgPersonNationalId);
originatingNaturalPerson.setCountryOfResidence("TZ");

// assign originator to person object
const originatingPerson = new ivms.ivms2023.Person();
originatingPerson.setNaturalPerson(originatingNaturalPerson);

// assign originator person to originator
const originator = new ivms.ivms2023.Originator();
originator.setOriginatorPerson([originatingPerson]);

// Beneficiary
// beneficiary 1 name id
const bene1NameId = new ivms.ivms2023.LegalPersonNameId();
bene1NameId.setLegalPersonName("ABC Limited");
bene1NameId.setLegalPersonNameIdentifierType(
  ivms.ivms2023.LegalPersonNameIdLegalPersonNameIdentifierTypeEnum.LEGL
);

// assign beneficiary 1 name with id
const bene1PersonName = new ivms.ivms2023.LegalPersonName();
bene1PersonName.setNameIdentifier([bene1NameId]);

// beneficiary 1 is a legal person
const beneficiary1LegalPerson = new ivms.ivms2023.LegalPerson();
beneficiary1LegalPerson.setName(bene1PersonName);

// assign beneficiary 1 to person object
const beneficiary1Person = new ivms.ivms2023.Person();
beneficiary1Person.setLegalPerson(beneficiary1LegalPerson);

// beneficiary 2 name id
const bene2NameId = new ivms.ivms2023.LegalPersonNameId();
bene2NameId.setLegalPersonName("CBA Trading");
bene2NameId.setLegalPersonNameIdentifierType(
  ivms.ivms2023.LegalPersonNameIdLegalPersonNameIdentifierTypeEnum.TRAD
);

// assign beneficiary 2 name with id
const bene2PersonName = new ivms.ivms2023.LegalPersonName();
bene2PersonName.setNameIdentifier([bene2NameId]);

// beneficiary 2 is a legal person
const beneficiary2LegalPerson = new ivms.ivms2023.LegalPerson();
beneficiary2LegalPerson.setName(bene2PersonName);

// assign beneficiary 2 to person object
const beneficiary2Person = new ivms.ivms2023.Person();
beneficiary2Person.setLegalPerson(beneficiary2LegalPerson);

// assign both persons to beneficiary object
const beneficiary = new ivms.ivms2023.Beneficiary();
beneficiary.setBeneficiaryPerson([beneficiary1Person, beneficiary2Person]);

// serialize originator and beneficiary to JSON
const originatorJson = originator.serializeToJson();
const beneficiaryJson = beneficiary.serializeToJson();

// create payload metadata
const payloadMetadata = new ivms.ivms2023.PayloadMetadata();
payloadMetadata.setPayloadVersion("1.0");

// combine into final payload
const privateInfo = {
  originator: originatorJson,
  beneficiary: beneficiaryJson,
  payloadMetadata: payloadMetadata.serializeToJson()
};

console.log(JSON.stringify(privateInfo, null, 2));

// decode from json data
const decodedOriginator = ivms.ivms2023.Originator.deserilizeFromJson(privateInfo.originator);
const decodedBeneficiary = ivms.ivms2023.Beneficiary.deserilizeFromJson(privateInfo.beneficiary);
console.log(JSON.stringify({
  originator: decodedOriginator.serializeToJson(),
  beneficiary: decodedBeneficiary.serializeToJson()
}, null, 2));
```