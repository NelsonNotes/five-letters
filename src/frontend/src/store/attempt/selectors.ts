import { TAttemptState } from '../../types/attempt'
import { RootState } from '../types'

export const selectAttempt = (state: RootState): TAttemptState => state.attempt
