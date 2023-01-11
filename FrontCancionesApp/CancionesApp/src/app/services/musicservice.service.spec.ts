import { TestBed } from '@angular/core/testing';

import { MusicserviceService } from './musicservice.service';

describe('MusicserviceService', () => {
  let service: MusicserviceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MusicserviceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
